# patterns.md — Example Topic File

<!--
This is an example of a topic file in the memory system.
Topic files hold detailed notes on a specific subject.
They are NOT loaded automatically — Claude reads them on demand.
Link to them from MEMORY.md so Claude knows they exist.

Keep entries concise and actionable. Organize by theme, not chronologically.
Remove entries that are no longer relevant.
-->

## Database

- PostgreSQL: always cast numpy types to native Python (`float()`, `int()`, `str()`) before inserts — psycopg2 can't serialize numpy types
- Use `RETURNING id` on inserts instead of a separate SELECT when you need the new row's ID
- Prefer `ON CONFLICT DO NOTHING` over checking existence first for idempotent ingestion pipelines

## Python

- Use `python3` not `python` on this machine
- Nested f-strings with triple quotes cause SyntaxError in Python 3.9 — build inner strings as separate variables first
- `dataclasses.field(default_factory=list)` for mutable default arguments, not `= []`

## TypeScript / Next.js

- Always run `tsc --noEmit` before committing — catches type errors the linter misses
- `use client` components can't use `async/await` directly — fetch in a server component and pass data as props

## Git

- Prefer `git commit --amend` only for the most recent unpushed commit — never amend published commits
- Use `git stash push -m "description"` not plain `git stash` so stashes are identifiable later
