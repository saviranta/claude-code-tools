# CLAUDE.md Snippet — Persistent Memory System

<!--
Paste the section below into your ~/.claude/CLAUDE.md.
Update the path to point to your actual memory repo.
-->

---

## Persistent Memory

Auto-memory is configured at `~/memory/`. `MEMORY.md` is loaded every session.

**When starting work on a project:**
1. Check `MEMORY.md` for relevant patterns and conventions
2. If continuing previous work, run `/memory continue`
3. Read topic files on demand (e.g. `~/memory/patterns.md`) for detailed notes

**When finishing work or switching tasks:**
- Run `/memory save` to write structured progress to `WORK_IN_PROGRESS.md` and push to GitHub
- Run `/memory commit` after updating any memory files

**When tokens are critically low:**
- Run `/memory save mini` — emergency save, minimal tokens, single git push

**What to save to memory:**
- Stable patterns and conventions confirmed across multiple sessions
- Key architectural decisions and important file paths
- Solutions to recurring problems
- User preferences for workflow and tools

**What NOT to save:**
- Session-specific context or in-progress state (use WORK_IN_PROGRESS.md for that)
- Unverified conclusions from a single file read
- Anything that duplicates instructions already in CLAUDE.md

---
