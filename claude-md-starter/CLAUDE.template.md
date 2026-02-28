# [Your Name]'s Claude Code Context

## Key Locations

<!--
List the directories Claude should always know about.
These are referenced throughout this file and in your conversations.
-->

| Location | Purpose |
|----------|---------|
| `~/projects/` | Active project development |
| `~/memory/` | Cross-session memory repo (see Persistent Memory section) |
| `~/notes/` | Personal notes vault (Obsidian, Notion, etc.) |

## Storage Philosophy

<!--
Define what goes where. Helps Claude understand your workspace layout
and avoid putting files in the wrong place.
-->

- **`~/memory/`** = Knowledge & Memory (GitHub-synced)
  - Session history, architecture docs, reusable prompts
  - Version controlled, searchable

- **`~/projects/`** = Active Development
  - Implementation code for each project
  - Each project gets its own subfolder and GitHub repo

## GitHub

- **Username**: your-github-username
- **Main memory repo**: `your-username/your-memory-repo`
- Use `gh` CLI for GitHub operations

## Projects

<!--
A quick-reference table of active projects.
Add a row for each project Claude might work on.
-->

| Project | Path | Description |
|---------|------|-------------|
| project-one | `~/projects/project-one/` | What it does |
| project-two | `~/projects/project-two/` | What it does |

## When Continuing Previous Work

<!--
Tell Claude how to recover context at the start of a session.
Adjust to match whatever memory system you use.
-->

If asked to continue a previous project or reference past work:
1. Check `~/memory/MEMORY.md` for session history
2. Check `~/memory/projects/` for project-specific docs

## User Preferences

<!--
Anything Claude should always do or never do.
Be specific — vague preferences are ignored.
-->

- [Add your preferences here]
- Example: Always use TypeScript strict mode
- Example: Prefer editing existing files over creating new ones
- Example: Ask before creating new directories

## MCP Servers

<!--
List MCP servers you have configured.
Remove this section if you don't use MCP.
Config location is typically ~/.claude.json
-->

| Server | Purpose |
|--------|---------|
| GitHub | GitHub API integration |

## Token Quota Management

<!--
What Claude should do when approaching context limits.
This prevents losing work mid-session.
-->

When you see a quota or usage limit warning:

1. **Save session summary**:
   - Add entry to `~/memory/MEMORY.md` with what was accomplished, decisions made, and next steps
   - Commit and push to GitHub

2. **Save project outputs**:
   - Save any generated code, docs, or artifacts to the relevant project folder

3. **Notify the user**:
   - Summarize what was saved and where
   - Explain how to continue in a new session

## Skills Available

<!--
List any Claude Code skills (/commands) you have configured.
Remove this section if you don't use custom skills.
-->

- `/memory` — Load context, search, commit session to GitHub
- `/your-skill` — What it does
