"""
Site Structure Analyzer

Reads your scraping-scope.md, fetches a sample page, and uses Claude
to identify page structure and generate a site-profile.json that the
scraper uses to know what to extract and what to ignore.

Usage:
    python site-structure-analyzer.py --url "https://example.com/items/123"
    python site-structure-analyzer.py --url "https://example.com/items/123" --scope scraping-scope.md
    python site-structure-analyzer.py --url "https://example.com/items/123" --output my-profile.json

Requirements:
    pip install anthropic playwright
    playwright install chromium
    export ANTHROPIC_API_KEY=your-key
"""

import argparse
import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import anthropic
from playwright.async_api import async_playwright


# ---------------------------------------------------------------------------
# Page fetching
# ---------------------------------------------------------------------------

async def fetch_page(url: str, headless: bool = True) -> str:
    """Fetch a fully-rendered page using Playwright."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1920, "height": 1080},
        )
        page = await context.new_page()

        print(f"  Loading {url}...")
        await page.goto(url, wait_until="networkidle", timeout=30000)

        # Dismiss cookie consent if present
        for label in ["Accept all", "Accept", "Accept cookies", "OK", "Agree"]:
            try:
                btn = page.locator(f'button:has-text("{label}")')
                if await btn.count() > 0:
                    await btn.first.click()
                    await page.wait_for_timeout(500)
                    break
            except Exception:
                pass

        # Scroll to trigger lazy-loaded content
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(1000)
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(300)

        html = await page.content()
        await browser.close()
        return html


def truncate_html(html: str, max_chars: int = 40000) -> str:
    """
    Truncate HTML for Claude's context window.
    Keeps head + first half (structure) and last portion (footer patterns).
    """
    if len(html) <= max_chars:
        return html
    half = max_chars // 2
    return html[:half] + "\n\n... [TRUNCATED FOR ANALYSIS] ...\n\n" + html[-half:]


# ---------------------------------------------------------------------------
# Scope reading
# ---------------------------------------------------------------------------

def read_scope(scope_path: Path) -> str:
    """Read the scraping scope markdown file if it exists."""
    if scope_path.exists():
        return scope_path.read_text(encoding="utf-8")
    return ""


# ---------------------------------------------------------------------------
# Claude analysis
# ---------------------------------------------------------------------------

def analyze_with_claude(html: str, scope: str, url: str) -> dict:
    """
    Send the page HTML and scope intent to Claude.
    Returns a structured site profile as a dict.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY environment variable not set.\n"
            "Export it with: export ANTHROPIC_API_KEY=your-key"
        )

    client = anthropic.Anthropic(api_key=api_key)
    domain = urlparse(url).netloc

    if scope:
        scope_block = (
            "The user has described their scraping intent below. "
            "Use this to decide which fields to extract and what to ignore.\n\n"
            f"<scraping_scope>\n{scope}\n</scraping_scope>"
        )
    else:
        scope_block = (
            "No scraping scope was provided. "
            "Perform a full structural analysis and identify all meaningful content fields."
        )

    prompt = f"""You are a web scraping specialist. Analyze the HTML structure of this page
and generate a JSON configuration profile that a Playwright scraper will use.

URL: {url}
Domain: {domain}

{scope_block}

Page HTML:
<html>
{html}
</html>

Generate a site profile JSON with this exact structure:

{{
  "domain": "{domain}",
  "analyzed_at": "PLACEHOLDER",
  "description": "<one sentence: what kind of page this is and what it shows>",
  "content": {{
    "main_selector": "<CSS selector for the primary content container>",
    "present_indicators": [
      "<visible text string that only appears when real content is loaded>",
      "<another indicator>"
    ],
    "removed_indicators": [
      "<regex pattern matching 404 or removed/unavailable messages>",
      "<another pattern>"
    ]
  }},
  "boilerplate": {{
    "exclude_selectors": [
      "<CSS selector for nav, header, footer, sidebars, ads, cookie banners>",
      "<more selectors to strip>"
    ]
  }},
  "fields": {{
    "<field_name>": {{
      "description": "<plain English: what this field contains>",
      "selector": "<CSS selector — prefer data attributes and semantic elements>",
      "type": "text|attribute|html",
      "attribute": "<attribute name, only if type is 'attribute'>"
    }}
  }},
  "scope_mode": "full|selective",
  "notes": "<any important observations: lazy loading, JS requirements, fragile selectors, etc.>"
}}

Rules:
- fields must reflect the user's stated capture intent (or all meaningful content if no scope)
- Prefer stable selectors: data-testid, data-label, semantic HTML over brittle class names
- Where selectors are uncertain, provide two options separated by a comma
- present_indicators must be visible text strings, not selectors
- removed_indicators must be valid Python regex patterns
- scope_mode is "selective" if the user wants specific fields only, "full" if they want everything
- Return only valid JSON — no markdown, no explanation text
"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = message.content[0].text.strip()

    # Strip markdown code fences if present
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        response_text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    profile = json.loads(response_text)
    profile["analyzed_at"] = datetime.now().isoformat()
    return profile


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------

async def analyze(
    url: str,
    scope_path: Path,
    output_path: Path,
    headless: bool = True,
) -> dict:
    """Fetch page, read scope, analyze with Claude, save site profile."""

    print(f"\nSite Structure Analyzer")
    print(f"{'─' * 40}")

    html = await fetch_page(url, headless=headless)
    print(f"  Fetched {len(html):,} bytes")

    scope = read_scope(scope_path)
    if scope:
        print(f"  Loaded scope: {scope_path}")
    else:
        print(f"  No scope file at {scope_path} — running full analysis")

    print(f"  Analyzing with Claude...")
    truncated = truncate_html(html)
    profile = analyze_with_claude(truncated, scope, url)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nProfile saved: {output_path}")
    print(f"{'─' * 40}")
    print(f"  Page type:   {profile.get('description', 'N/A')}")
    print(f"  Main area:   {profile['content'].get('main_selector', 'N/A')}")
    print(f"  Fields:      {', '.join(profile.get('fields', {}).keys()) or 'none'}")
    print(f"  Strip:       {len(profile['boilerplate'].get('exclude_selectors', []))} boilerplate selectors")
    print(f"  Mode:        {profile.get('scope_mode', 'full')}")
    if profile.get("notes"):
        print(f"  Notes:       {profile['notes']}")
    print()

    return profile


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a website's structure to generate a scraping profile",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--url", required=True, help="A sample page URL to analyze")
    parser.add_argument(
        "--scope",
        default="scraping-scope.md",
        help="Scraping scope file (default: scraping-scope.md)",
    )
    parser.add_argument(
        "--output",
        default="site-profile.json",
        help="Output path for the site profile (default: site-profile.json)",
    )
    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Show the browser window during analysis",
    )
    args = parser.parse_args()

    asyncio.run(
        analyze(
            url=args.url,
            scope_path=Path(args.scope),
            output_path=Path(args.output),
            headless=not args.no_headless,
        )
    )


if __name__ == "__main__":
    main()
