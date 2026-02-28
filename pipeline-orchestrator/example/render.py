"""
Example tool: render

Reads structured data from the database and generates output —
a report, HTML file, JSON export, dashboard, or anything else.
Runs after parse.

This module is registered in TOOL_MAP as "render" and belongs
to the "render" and "full" stage groups.
"""

from pathlib import Path


OUTPUT_DIR = Path("output")


def run(conn, **kwargs) -> None:
    """
    Generate output from structured data.

    Args:
        conn:    Database connection from get_connection()
        **kwargs: Any extra arguments passed via the CLI or _run_tool()
    """
    print("  Rendering output...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Example: read from DB
    # with conn.cursor() as cur:
    #     cur.execute("SELECT id, name, price, tags FROM items ORDER BY price")
    #     items = cur.fetchall()
    # print(f"  Rendering {len(items)} items")

    # Example: write JSON export
    # import json
    # output = [dict(row) for row in items]
    # (OUTPUT_DIR / "items.json").write_text(json.dumps(output, indent=2))
    # print(f"  Saved output/items.json")

    # Example: write simple HTML report
    # rows = "\n".join(
    #     f"<tr><td>{r['name']}</td><td>${r['price']:.2f}</td></tr>"
    #     for r in items
    # )
    # html = f"""<!DOCTYPE html>
    # <html><body>
    # <h1>Items Report</h1>
    # <table>{rows}</table>
    # </body></html>"""
    # (OUTPUT_DIR / "report.html").write_text(html)
    # print(f"  Saved output/report.html")

    print("  render: replace this with your output generation logic")
