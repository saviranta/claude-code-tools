"""
Pipeline Orchestrator

Runs multi-stage data pipelines where each stage is a Python module
exposing a run(conn, **kwargs) function. Stages can be run individually,
in groups, or as a full pipeline — all from a single CLI entry point.

Usage:
    python orchestrator.py                  # Run full pipeline
    python orchestrator.py ingest           # Run a single stage
    python orchestrator.py fetch parse      # Run specific tools in order
    python orchestrator.py analyze render   # Run a stage group
    python orchestrator.py --list           # Show available stages and tools

Setup:
    1. Copy this file into your project root
    2. Register your tools in TOOL_MAP below (module path → tool name)
    3. Define your stage groups in STAGES below
    4. Each tool module must expose: def run(conn, **kwargs) -> None
    5. Update get_connection() to return your database connection
"""

import argparse
import importlib
import sys
import time
from pathlib import Path

# Ensure project root is on the Python path
sys.path.insert(0, str(Path(__file__).parent))


# ---------------------------------------------------------------------------
# Database connection
# ---------------------------------------------------------------------------

def get_connection():
    """
    Return a database connection.
    Replace this with your actual connection logic.

    Examples:
        PostgreSQL:  import psycopg2; return psycopg2.connect(os.environ["DATABASE_URL"])
        SQLite:      import sqlite3; return sqlite3.connect("data.db")
        No DB:       return None  (and remove conn from tool signatures)
    """
    raise NotImplementedError(
        "Implement get_connection() to return your database connection.\n"
        "See the docstring above for examples."
    )


# ---------------------------------------------------------------------------
# Tool registry
# ---------------------------------------------------------------------------
# Maps tool names to their module paths.
# Each module must expose: def run(conn, **kwargs) -> None
#
# Example module path formats:
#   'src.pipeline.fetch'     → src/pipeline/fetch.py
#   'tools.parse'            → tools/parse.py
#   'example.fetch'          → example/fetch.py

TOOL_MAP = {
    # --- Ingest ---
    "fetch":     "example.fetch",
    # --- Process ---
    "parse":     "example.parse",
    # --- Output ---
    "render":    "example.render",
    # Add your tools here:
    # "my_tool": "src.my_module",
}


# ---------------------------------------------------------------------------
# Stage groups
# ---------------------------------------------------------------------------
# Stages are named groups of tools that run in sequence.
# "full" is the default and runs everything.

STAGES = {
    "ingest":   ["fetch"],
    "process":  ["parse"],
    "render":   ["render"],
    "full":     ["fetch", "parse", "render"],
}


# ---------------------------------------------------------------------------
# Core runner
# ---------------------------------------------------------------------------

def _run_tool(name: str, conn, **kwargs) -> None:
    """Import a tool module by name and call its run() function."""
    if name not in TOOL_MAP:
        print(f"\nUnknown tool: {name}")
        print(f"Available tools: {', '.join(sorted(TOOL_MAP.keys()))}")
        sys.exit(1)

    module_path = TOOL_MAP[name]
    print(f"\n{'─' * 50}")
    print(f"  {name}  ({module_path})")
    print(f"{'─' * 50}")

    module = importlib.import_module(module_path)

    if not hasattr(module, "run"):
        print(f"Error: {module_path} has no run() function.")
        print("Each tool module must expose: def run(conn, **kwargs) -> None")
        sys.exit(1)

    start = time.time()
    module.run(conn, **kwargs)
    elapsed = time.time() - start
    print(f"  Done ({elapsed:.1f}s)")


def _list_tools() -> None:
    """Print available stages and tools."""
    print("\nStage groups:")
    for stage, tools in STAGES.items():
        print(f"  {stage:<15} → {', '.join(tools)}")
    print(f"\nIndividual tools:")
    print(f"  {', '.join(sorted(TOOL_MAP.keys()))}")


def _resolve_targets(targets: list[str]) -> list[str]:
    """Expand stage names into tool lists, deduplicate, preserve order."""
    tools = []
    for target in targets:
        if target in STAGES:
            tools.extend(STAGES[target])
        else:
            tools.append(target)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in tools:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    return unique


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pipeline Orchestrator — run data pipeline stages from the CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "targets",
        nargs="*",
        default=["full"],
        help="Stage names or tool names to run (default: full)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available stages and tools",
    )
    args = parser.parse_args()

    if args.list:
        _list_tools()
        return

    tools = _resolve_targets(args.targets)
    print(f"\nPipeline: {' → '.join(tools)}")

    conn = get_connection()
    total_start = time.time()

    try:
        for tool_name in tools:
            _run_tool(tool_name, conn)

    except KeyboardInterrupt:
        print("\n\nInterrupted.")
        sys.exit(1)

    finally:
        if hasattr(conn, "close"):
            conn.close()

    total = time.time() - total_start
    print(f"\n{'─' * 50}")
    print(f"  All done  ({total:.1f}s total)")
    print(f"{'─' * 50}\n")


if __name__ == "__main__":
    main()
