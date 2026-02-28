"""
Example tool: fetch

Ingests raw data from a source and writes it to the database.
Replace the body of run() with your actual ingestion logic.

This module is registered in TOOL_MAP as "fetch" and belongs
to the "ingest" and "full" stage groups.
"""


def run(conn, **kwargs) -> None:
    """
    Fetch raw data from a source and store it.

    Args:
        conn:    Database connection from get_connection()
        **kwargs: Any extra arguments passed via the CLI or _run_tool()
    """
    print("  Fetching data from source...")

    # Example: read from a CSV file
    # import csv
    # with open("data/input.csv") as f:
    #     rows = list(csv.DictReader(f))
    # print(f"  Read {len(rows)} rows")

    # Example: call an API
    # import httpx
    # response = httpx.get("https://api.example.com/items")
    # items = response.json()["items"]

    # Example: insert into DB
    # with conn.cursor() as cur:
    #     for item in items:
    #         cur.execute(
    #             "INSERT INTO raw_items (id, data) VALUES (%s, %s) ON CONFLICT DO NOTHING",
    #             (item["id"], json.dumps(item))
    #         )
    # conn.commit()
    # print(f"  Stored {len(items)} items")

    print("  fetch: replace this with your ingestion logic")
