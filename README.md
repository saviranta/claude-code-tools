# claude-code-tools

Reusable tools, patterns, and configurations for Claude Code. These are Claude Code–specific — they use features like hooks, skills, CLAUDE.md, and MCP integrations. Each tool is self-contained with its own README and usage guide.

## Tools

| Tool | Description |
|------|-------------|
| `persistent-memory-system/` | Use a GitHub repo as external cross-session memory for Claude Code: MEMORY.md structure, topic files, `/memory` skill, and token-quota-triggered save protocol |
| `claude-md-starter/` | Opinionated CLAUDE.md template covering project layout, preferences, MCP config, token management, and skill definitions |
| `agentic-architecture-generator/` | Meta-prompt that documents any agentic system as a structured architecture doc (tools, orchestration, state flow, review gates) |
| `playwright-web-scraper/` | Playwright-based web scraper with retry logic, HTML extraction, and structured field parsing — designed for use inside Claude Code agentic pipelines |
| `gmail-mcp-url-extractor/` | Extracts structured data (URLs, metadata) from Gmail alerts via MCP — useful for triggering downstream automation from email notifications |
| `html-pipeline-orchestrator/` | Multi-step analysis pipeline pattern: ingest → analyze → render → serve, with a clean separation between data and presentation layers |

## Design principles

**Claude Code–native.** These tools assume Claude Code as the runtime. They use `.claudecode` project context, skill definitions, hooks, and CLAUDE.md conventions — not just raw prompts.

**Self-contained.** Each tool folder has everything needed to understand and use it: prompt or config, example, and a README explaining inputs, outputs, and integration points.

**No lock-in on the pattern.** While implemented for Claude Code, most patterns (memory system, pipeline orchestrator) are adaptable to other agentic runtimes.

## Structure

```
claude-code-tools/
├── persistent-memory-system/
├── claude-md-starter/
├── agentic-architecture-generator/
├── playwright-web-scraper/
├── gmail-mcp-url-extractor/
└── html-pipeline-orchestrator/
```

Each tool folder contains:
- `README.md` — what it does, when to use it, how to set it up
- Core files (prompt, config, skill definition, or script)
- `example/` — worked example

## Related

- [pm-tools](https://github.com/saviranta/PM-tools) — LLM workflows for product management
- [job-tools](https://github.com/saviranta/job-tools) — Tools for job search and applications
