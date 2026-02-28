# Pipeline Orchestrator

A lightweight CLI orchestrator for multi-stage data pipelines. Register your pipeline tools as Python modules, define stage groups, and run any combination from a single entry point.

```
python orchestrator.py                  # full pipeline
python orchestrator.py ingest           # one stage
python orchestrator.py fetch parse      # specific tools in order
python orchestrator.py --list           # show what's available
```

## When to use this

This pattern is useful when your pipeline has multiple distinct stages that you want to run independently or in sequence — for example: fetch data → parse and clean → enrich → analyze → render output. Without an orchestrator, you end up with a collection of scripts that are hard to run in the right order or partially re-run when something fails.

## Files

```
pipeline-orchestrator/
├── orchestrator.py       — the orchestrator (copy this into your project)
└── example/
    ├── fetch.py          — example: ingest raw data from a source
    ├── parse.py          — example: transform raw data into structured records
    └── render.py         — example: generate output from structured data
```

## Setup

### 1. Copy orchestrator.py into your project root

```
my-project/
├── orchestrator.py
├── src/
│   ├── pipeline/
│   │   ├── fetch.py
│   │   ├── parse.py
│   │   └── render.py
│   └── analysis/
│       └── summarize.py
└── output/
```

### 2. Configure your database connection

Open `orchestrator.py` and implement `get_connection()`:

```python
def get_connection():
    import psycopg2, os
    return psycopg2.connect(os.environ["DATABASE_URL"])
```

For SQLite:
```python
def get_connection():
    import sqlite3
    return sqlite3.connect("data.db")
```

If your pipeline doesn't use a database, return `None` and remove `conn` from your tool signatures.

### 3. Register your tools

In `orchestrator.py`, add your tools to `TOOL_MAP`:

```python
TOOL_MAP = {
    "fetch":     "src.pipeline.fetch",
    "parse":     "src.pipeline.parse",
    "enrich":    "src.pipeline.enrich",
    "summarize": "src.analysis.summarize",
    "render":    "src.pipeline.render",
}
```

The key is the CLI name. The value is the Python module path (dots, not slashes).

### 4. Define your stage groups

```python
STAGES = {
    "ingest":   ["fetch", "parse"],
    "analyze":  ["enrich", "summarize"],
    "render":   ["render"],
    "full":     ["fetch", "parse", "enrich", "summarize", "render"],
}
```

`full` is the default when no target is specified.

### 5. Implement the tool contract

Each tool module must expose a `run()` function:

```python
def run(conn, **kwargs) -> None:
    # conn: database connection from get_connection()
    # **kwargs: any extra args from the CLI or _run_tool()
    ...
```

See the `example/` folder for working templates.

## Running the pipeline

```bash
# Full pipeline (runs the "full" stage group)
python orchestrator.py

# A single stage group
python orchestrator.py ingest
python orchestrator.py analyze

# Specific tools in a custom order
python orchestrator.py fetch enrich render

# List everything available
python orchestrator.py --list
```

## Passing arguments to tools

Add CLI flags in `main()` and thread them through `_run_tool()`:

```python
# In main():
parser.add_argument("--since", help="Only process records since this date")

# In the run loop:
_run_tool(tool_name, conn, since=args.since)

# In your tool:
def run(conn, since=None, **kwargs):
    query = "SELECT * FROM items"
    if since:
        query += f" WHERE created_at > '{since}'"
    ...
```

## How it works

1. CLI parses targets (stage names or tool names)
2. Stage names are expanded into their tool lists
3. Duplicates are removed while preserving order
4. Tools run sequentially, sharing a single DB connection
5. Connection is closed cleanly on completion or interrupt
