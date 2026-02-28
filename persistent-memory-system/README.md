# Persistent Memory System for Claude Code

A pattern for giving Claude Code persistent memory across sessions using a GitHub repo, a structured `MEMORY.md`, and a `/memory` skill.

## The problem

Claude Code has no memory between sessions. Every conversation starts blank. You re-explain your project structure, preferences, and context every time.

## The solution

A GitHub repo acts as external long-term memory. Claude reads a `MEMORY.md` at the start of each session (via Claude Code's auto-memory feature) and writes to it when work is done. A `/memory` skill provides commands for loading context, saving progress, and committing to GitHub.

```
┌─────────────────────────────────────────┐
│            YOUR MEMORY REPO             │
│                                         │
│  MEMORY.md          ← Claude reads this │
│  WORK_IN_PROGRESS.md ← save/continue   │
│  patterns.md        ← topic files       │
│  debugging.md       ← topic files       │
└─────────────────────────────────────────┘
         ↑ git push        ↓ auto-memory
┌─────────────────────────────────────────┐
│            CLAUDE CODE SESSION          │
│                                         │
│  /memory load    → read context         │
│  /memory save    → save progress        │
│  /memory commit  → push to GitHub       │
└─────────────────────────────────────────┘
```

## Setup

### 1. Create your memory repo

```bash
mkdir ~/memory
cd ~/memory
git init
git remote add origin https://github.com/your-username/your-memory-repo.git
```

Copy `MEMORY.template.md` → `MEMORY.md` and fill in your initial context.

### 2. Enable auto-memory in Claude Code

Claude Code supports an auto-memory directory — files there are loaded automatically each session. Configure it by adding to `~/.claude.json`:

```json
{
  "autoMemoryDir": "~/memory"
}
```

Claude will read `MEMORY.md` from that directory at the start of every session. Lines after 200 are truncated, so keep it concise.

### 3. Install the /memory skill

Copy `commands/memory.md` to `~/.claude/commands/memory.md`.

Then update the paths inside it to point to your memory repo (search for `~/memory/` and replace with your actual path).

### 4. Add the CLAUDE.md snippet

Copy the content of `CLAUDE.snippet.md` into your `~/.claude/CLAUDE.md` to tell Claude how to use the memory system.

## How it works in practice

### Starting a session
```
/memory          # loads INDEX.md + MEMORY.md, summarizes context
```

### During a session
Claude reads `MEMORY.md` automatically. For topic-specific detail, you can ask Claude to read a specific topic file (e.g. `~/memory/patterns.md`).

### Saving progress

**Full save** — use when finishing work or switching tasks:
```
/memory save
```
Analyzes the session, writes a structured entry to `WORK_IN_PROGRESS.md` (purpose, completed, next steps, key files, how to continue), and commits to GitHub.

**Mini save** — use when tokens are critically low:
```
/memory save mini
```
Emergency mode: no file reading, minimal output, single write + git push. Just enough to continue next session.

### Continuing work next session
```
/memory continue
```
Reads `WORK_IN_PROGRESS.md`, shows saved entries, and loads the relevant context.

### Committing updates
```
/memory commit
```
Stages all changes and pushes to GitHub.

## MEMORY.md structure

Keep `MEMORY.md` short (under 150 lines — it's loaded every session). Use it for:
- Stable patterns and conventions
- Key architectural decisions and important paths
- User preferences
- Solutions to recurring problems

For longer notes, create topic files (`patterns.md`, `debugging.md`, etc.) and link to them from `MEMORY.md`. Claude reads topic files on demand, not automatically.

See `MEMORY.template.md` and `example-topic.md` for the format.

## What to save vs. what not to save

**Save:**
- Patterns confirmed across multiple interactions
- Key architectural decisions
- User preferences for tools and workflow
- Solutions to recurring problems

**Don't save:**
- Session-specific context (current task details, in-progress state)
- Unverified conclusions from reading a single file
- Anything that duplicates CLAUDE.md instructions

## Files in this tool

```
persistent-memory-system/
├── README.md                    ← this file
├── MEMORY.template.md           ← starter MEMORY.md
├── WORK_IN_PROGRESS.template.md ← starter WORK_IN_PROGRESS.md
├── example-topic.md             ← example of a topic file
├── CLAUDE.snippet.md            ← paste this into your CLAUDE.md
└── commands/
    └── memory.md                ← the /memory skill definition
```

## Related

- [claude-md-starter](../claude-md-starter/) — CLAUDE.md template that includes the memory system snippet
