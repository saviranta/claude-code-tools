"""
Example tool: parse

Reads raw data from the database, transforms it into structured records,
and writes the results back. Runs after fetch.

This module is registered in TOOL_MAP as "parse" and belongs
to the "process" and "full" stage groups.
"""


def run(conn, **kwargs) -> None:
    """
    Parse and transform raw data into structured records.

    Args:
        conn:    Database connection from get_connection()
        **kwargs: Any extra arguments passed via the CLI or _run_tool()
    """
    print("  Parsing raw data...")

    # Example: read unparsed rows from DB
    # with conn.cursor() as cur:
    #     cur.execute("SELECT id, data FROM raw_items WHERE parsed_at IS NULL")
    #     rows = cur.fetchall()
    # print(f"  Found {len(rows)} unparsed items")

    # Example: parse each row
    # parsed = []
    # for row in rows:
    #     raw = json.loads(row["data"])
    #     parsed.append({
    #         "id":    raw["id"],
    #         "name":  raw["title"].strip(),
    #         "price": float(raw["price"].replace("$", "").replace(",", "")),
    #         "tags":  [t.lower() for t in raw.get("tags", [])],
    #     })

    # Example: write structured records
    # with conn.cursor() as cur:
    #     for item in parsed:
    #         cur.execute("""
    #             INSERT INTO items (id, name, price, tags)
    #             VALUES (%s, %s, %s, %s)
    #             ON CONFLICT (id) DO UPDATE SET
    #                 name = EXCLUDED.name,
    #                 price = EXCLUDED.price,
    #                 tags = EXCLUDED.tags,
    #                 parsed_at = NOW()
    #         """, (item["id"], item["name"], item["price"], item["tags"]))
    # conn.commit()
    # print(f"  Parsed and stored {len(parsed)} items")

    print("  parse: replace this with your transformation logic")
