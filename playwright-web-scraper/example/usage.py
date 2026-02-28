"""
Usage examples for playwright-web-scraper.

Before running:
    pip install -r requirements.txt
    playwright install chromium
    export ANTHROPIC_API_KEY=your-key  # only needed for site-structure-analyzer
"""

import asyncio
from pathlib import Path
from scraper import scrape_sync, scrape_multiple, load_site_profile, html_exists, list_saved


URL_TEMPLATE = "https://example.com/items/{id}"


# ---------------------------------------------------------------------------
# Example 1: Scrape a single item (no profile)
# ---------------------------------------------------------------------------

def example_single():
    result = scrape_sync("item-123", url_template=URL_TEMPLATE)

    if result.status == "success":
        print(f"Success: {result.bytes:,} bytes saved to output/item-123.html")
    elif result.status == "removed":
        print(f"Item has been removed: {result.error_message}")
    else:
        print(f"Error: {result.error_message}")


# ---------------------------------------------------------------------------
# Example 2: Analyze site first, then scrape with profile
# ---------------------------------------------------------------------------

def example_with_profile():
    # Step 1 (run once): python site-structure-analyzer.py --url "https://example.com/items/123"
    # This generates site-profile.json

    # Step 2: Load profile and scrape
    profile = load_site_profile()  # reads site-profile.json if it exists

    if profile:
        print(f"Using site profile for: {profile['domain']}")
        print(f"Fields: {', '.join(profile.get('fields', {}).keys())}")
    else:
        print("No site profile found — scraping without structural guidance")

    result = scrape_sync("item-123", url_template=URL_TEMPLATE, site_profile=profile)
    print(f"Status: {result.status}")


# ---------------------------------------------------------------------------
# Example 3: Scrape multiple items with deduplication
# ---------------------------------------------------------------------------

async def example_batch():
    item_ids = ["item-001", "item-002", "item-003", "item-004", "item-005"]

    # Skip items we've already scraped
    pending = [id for id in item_ids if not html_exists(id)]
    print(f"Scraping {len(pending)} of {len(item_ids)} items ({len(item_ids) - len(pending)} already saved)")

    results = await scrape_multiple(
        pending,
        url_template=URL_TEMPLATE,
        delay_ms=2000,   # 2 seconds between requests
        max_retries=3,
    )

    success = [id for id, r in results.items() if r.status == "success"]
    removed = [id for id, r in results.items() if r.status == "removed"]
    errors  = [id for id, r in results.items() if r.status == "error"]

    print(f"\nResults: {len(success)} success, {len(removed)} removed, {len(errors)} error")
    print(f"Total saved: {len(list_saved())} HTML files in output/")


# ---------------------------------------------------------------------------
# Example 4: Re-use saved HTML without re-scraping
# ---------------------------------------------------------------------------

def example_reuse_saved():
    from scraper import load_saved_html

    html = load_saved_html("item-123")
    if html:
        print(f"Loaded saved HTML: {len(html):,} bytes")
        # Parse it however you like — BeautifulSoup, regex, etc.
    else:
        print("No saved HTML for item-123 — scrape it first")


if __name__ == "__main__":
    print("=== Example 1: Single scrape ===")
    example_single()

    print("\n=== Example 2: With site profile ===")
    example_with_profile()

    print("\n=== Example 3: Batch scrape ===")
    asyncio.run(example_batch())

    print("\n=== Example 4: Re-use saved HTML ===")
    example_reuse_saved()
