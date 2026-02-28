# Playwright Web Scraper

A Playwright-based scraper for dynamic, JavaScript-rendered pages. Handles 403 backoff, timeouts, cookie consent, and lazy-loaded content out of the box.

Pairs with a **site structure analyzer** that reads a plain-language scope file and uses Claude to generate a scraping profile — so the scraper knows what content to target and what boilerplate to ignore.

## Files

```
playwright-web-scraper/
├── scraper.py                      — main scraper
├── site-structure-analyzer.py      — generates site-profile.json from scope + page
├── scraping-scope.template.md      — define what to scrape in plain language
├── requirements.txt
└── example/
    ├── usage.py                    — working code examples
    ├── scraping-scope.example.md   — filled-in scope example
    └── site-profile.example.json   — example analyzer output
```

Scraped HTML is saved to:
```
output/
└── {item_id}.html    — raw HTML per scraped page
```

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
export ANTHROPIC_API_KEY=your-key   # only needed for site-structure-analyzer
```

## Recommended flow

### 1. Define your scope (optional but recommended)

Copy `scraping-scope.template.md` → `scraping-scope.md` and fill it in plain language:

```markdown
## What kind of page are you scraping?
An e-commerce product page showing a single item for sale.

## What do you want to capture?
Product name, price, sizes in stock, description, and customer rating.

## What should be ignored?
Header navigation, footer, cookie banner, related products, and ads.

## How much of the page?
Specific content only.
```

No CSS selectors needed — the analyzer handles that.

### 2. Analyze the site (run once per site)

Point the analyzer at a real sample page:

```bash
python site-structure-analyzer.py --url "https://example.com/products/123"
```

This fetches the page, reads your scope, and uses Claude to identify the page structure. Saves `site-profile.json` with:
- CSS selectors for each field you want to capture
- Selectors for boilerplate to strip (nav, footer, ads)
- Text indicators confirming real content is present
- Regex patterns detecting removed/unavailable pages

Review `site-profile.json` — it's readable JSON and you can tweak selectors if needed.

### 3. Scrape

```python
from scraper import scrape_sync, load_site_profile

profile = load_site_profile()  # reads site-profile.json

result = scrape_sync("product-123", url_template="https://example.com/products/{id}",
                     site_profile=profile)

if result.status == "success":
    print(f"Saved {result.bytes:,} bytes to output/product-123.html")
```

Raw HTML is saved to `output/{item_id}.html` automatically.

## Scraping without a profile

The scraper works without a site profile — just skip steps 1 and 2:

```python
from scraper import scrape_sync

result = scrape_sync("item-123", url_template="https://example.com/items/{id}")
```

You lose the structural guidance (field targeting, boilerplate stripping) but the retry logic, cookie handling, and HTML saving all still work.

## Batch scraping

```python
import asyncio
from scraper import scrape_multiple

results = asyncio.run(
    scrape_multiple(
        ["item-001", "item-002", "item-003"],
        url_template="https://example.com/items/{id}",
        delay_ms=2000,   # polite delay between requests
    )
)
```

## Result statuses

| Status | Meaning |
|--------|---------|
| `success` | Page scraped, HTML saved |
| `removed` | Item no longer available (404, redirect, or removal text detected) |
| `error` | Scrape failed (timeout, repeated 403, unexpected exception) |

## Re-using saved HTML

Saved HTML can be re-parsed without re-scraping:

```python
from scraper import html_exists, load_saved_html, list_saved

# Check before scraping
if not html_exists("item-123"):
    result = scrape_sync("item-123", url_template=...)

# Load saved HTML
html = load_saved_html("item-123")

# List all saved items
ids = list_saved()
```

## Configuring indicators manually

If you're not using a site profile, pass indicators directly:

```python
result = scrape_sync(
    "item-123",
    url_template="https://example.com/items/{id}",
    present_indicators=["Add to cart", "In stock"],     # confirms real content
    removed_indicators=[r"item.*not found", r"sold out"],  # regex
)
```

## Analyzer options

```bash
# Use a different scope file
python site-structure-analyzer.py --url "..." --scope my-scope.md

# Save profile to a custom path
python site-structure-analyzer.py --url "..." --output profiles/my-site.json

# Show browser window during analysis
python site-structure-analyzer.py --url "..." --no-headless
```
