# claude-code-tools

Reusable tools, patterns, and configurations for Claude Code. These are Claude Code–specific — they use features like hooks, skills, CLAUDE.md, and MCP integrations. Each tool is self-contained with its own README and usage guide.

## Design principles

**Claude Code–native.** These tools assume Claude Code as the runtime. They use `.claudecode` project context, skill definitions, hooks, and CLAUDE.md conventions — not just raw prompts.

**Self-contained.** Each tool folder has everything needed to understand and use it: prompt or config, example, and a README explaining inputs, outputs, and integration points.

**No lock-in on the pattern.** While implemented for Claude Code, most patterns (memory system, pipeline orchestrator) are adaptable to other agentic runtimes.


## Related

- [pm-tools](https://github.com/saviranta/PM-tools) — LLM workflows for product management
- [job-tools](https://github.com/saviranta/job-tools) — Tools for job search and applications
