# claude-md-starter

A starter template for `CLAUDE.md` — the persistent context file that Claude Code reads at the start of every session.

## What is CLAUDE.md?

`CLAUDE.md` is a markdown file that Claude Code automatically loads as context. It tells Claude about your workspace, preferences, projects, and workflows so you don't have to re-explain them every session.

There are two scopes:

| File | Scope |
|------|-------|
| `~/.claude/CLAUDE.md` | Global — applies to every Claude Code session on your machine |
| `<project-root>/CLAUDE.md` | Project-local — applies only when working in that directory |

Start with a global one. Add project-local ones for repos with specific conventions.

## How to use the template

1. Copy [`CLAUDE.template.md`](CLAUDE.template.md) to `~/.claude/CLAUDE.md`
2. Fill in your own values — paths, projects, GitHub username, preferences
3. Delete sections you don't need
4. Reload Claude Code — it picks up changes immediately

## What each section does

**Key Locations** — A reference table of important directories. Claude uses these throughout conversations so you can say "save it to the projects folder" without spelling out the full path every time.

**Storage Philosophy** — Defines what goes where. Useful if you separate code from memory from notes across multiple folders or repos.

**GitHub** — Your username and primary repos. Lets Claude use the `gh` CLI correctly without asking every time.

**Projects** — Quick-reference table of active projects with paths and descriptions. Claude uses this to orient itself when you say "let's work on project X".

**When Continuing Previous Work** — Instructions for how to recover context at the start of a session. Pair this with a [persistent memory system](../persistent-memory-system/) for best results.

**User Preferences** — Anything Claude should always or never do. Be specific. "Write clean code" does nothing; "always use TypeScript strict mode" and "ask before creating new files" are actionable.

**MCP Servers** — Documents which MCP servers you have configured and what they're for. Helps Claude know what tools are available without you having to mention them.

**Token Quota Management** — What Claude should do when approaching context limits. Without this, work can be lost mid-session. With it, Claude saves progress and tells you how to continue.

**Skills Available** — Documents any custom `/skills` you've configured so Claude knows to suggest them when relevant.

## Tips

- **Keep it short.** Claude reads the whole file every session. Long files add latency and dilute what matters. Aim for under 150 lines.
- **Be specific in preferences.** Vague instructions are ignored. Concrete ones are followed.
- **Use it as a contract.** If you find yourself repeatedly correcting the same behavior, add it here.
- **Iterate.** Start minimal, add sections as you notice gaps. Don't try to anticipate everything upfront.

## Related

- [persistent-memory-system](../persistent-memory-system/) — Cross-session memory using a GitHub repo
- [agentic-architecture-generator](../agentic-architecture-generator/) — Generate full architecture docs for any agent
