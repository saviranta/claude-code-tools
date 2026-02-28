# /memory - Persistent Memory System

Access and manage your Claude Code memory repo.

## Usage

```
/memory                     # Load context (INDEX.md + MEMORY.md)
/memory search <query>      # Search all memory files for a term
/memory add <content>       # Add an entry to MEMORY.md
/memory save                # Save current session progress (full)
/memory save mini           # Emergency save — minimal tokens
/memory continue            # Resume work from a previous session
/memory commit [message]    # Commit all changes and push to GitHub
/memory pull                # Pull latest from GitHub
/memory push                # Push local commits to GitHub
/memory status              # Show git status
/memory log                 # Show recent commits
```

## Configuration

Set `MEMORY_REPO` to your local memory repo path:

```
MEMORY_REPO=~/memory
```

Update all path references below to match.

---

## Instructions

### No argument / "load" / "context"

Read and display:
1. `$MEMORY_REPO/INDEX.md` — structure overview (if it exists)
2. `$MEMORY_REPO/MEMORY.md` — patterns, preferences, active projects

Summarize key points for the user. Do not dump the full file contents.

### "search \<query\>"

Run:
```bash
grep -r -i -n "<query>" ~/memory/ --include="*.md" | head -30
```

Show file:line:match results. Do NOT read full files — just show grep output.

### "add \<content\>"

Append a new entry to `$MEMORY_REPO/MEMORY.md` under the relevant section with today's date. Then offer to commit.

### "save"

Full save. Use when finishing work or switching tasks.

1. **Analyze the current session** to determine:
   - Project name
   - Goal / purpose of the work
   - What was completed
   - What remains (next steps)
   - Key files involved

2. **Append to `$MEMORY_REPO/WORK_IN_PROGRESS.md`**:

```markdown
## [Project Name] - [Brief Description]
**Saved**: YYYY-MM-DD HH:MM
**Status**: in_progress

### Purpose
[What is the goal of this work]

### Completed
- [What has been done]

### Next Steps
- [What remains to be done]

### Key Files
- [List of relevant files/paths]

### How to Continue
[Specific instructions for resuming]

---
```

3. **Commit and push**:
```bash
cd ~/memory && git add -A && git commit -m "WIP: Save progress on [project]" && git push origin main
```

4. Confirm to user what was saved and how to continue next session.

### "save mini"

Emergency save when tokens are critically low. No reading, no analysis, pure speed.

**Rules:**
- NO reading files
- NO analyzing the session
- MINIMAL output
- SINGLE write operation

**Action:** Immediately append to `$MEMORY_REPO/WORK_IN_PROGRESS.md`:

```markdown
## QUICK SAVE - [current date/time]
Project: [project name from conversation]
Task: [one line — what were we doing]
Next: [one line — what to do next]
Files: [comma-separated key file paths]
---
```

Then run:
```bash
cd ~/memory && git add WORK_IN_PROGRESS.md && git commit -m "WIP quick save" && git push origin main
```

**Output to user:** Just "Saved. Run `/memory continue` next session."

### "continue"

Resume work from a previous session.

1. Read `$MEMORY_REPO/WORK_IN_PROGRESS.md`

2. **If empty or missing:** Tell user "No work in progress found."

3. **If one entry:** Show summary, ask "Continue with [project]?", then follow the "How to Continue" instructions and read key files.

4. **If multiple entries:** List them:
   ```
   Found multiple works in progress:
   1. [Project A] — [description] (saved YYYY-MM-DD)
   2. [Project B] — [description] (saved YYYY-MM-DD)

   Which would you like to continue?
   ```
   Wait for user choice, then load that context.

5. After resuming, mark the entry status as "resumed" with timestamp. Don't delete it.

### "commit [message]"

```bash
cd ~/memory && git add -A && git status
```

If no message provided, generate one from the changes. Then:

```bash
git commit -m "<message>" && git push origin main
```

Confirm success.

### "pull"
```bash
cd ~/memory && git pull origin main
```

### "push"
```bash
cd ~/memory && git push origin main
```

### "status"
```bash
cd ~/memory && git status
```

### "log"
```bash
cd ~/memory && git log --oneline -10
```

---

## Token efficiency notes

| Command | Approach |
|---------|----------|
| `search` | grep only — no full file reads |
| `load` | Reads 2 files, summarizes |
| `save` | Analyzes session, writes one file, commits |
| `save mini` | No reading, minimal write, single git command |
| `continue` | Reads WIP file only, loads relevant context |
| `commit/pull/push` | Git only, no file reading |
