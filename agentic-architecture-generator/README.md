# Agentic Architecture Generator

A prompt that turns your agent idea into a complete architecture document through a structured two-phase conversation with Claude.

## What you get

An 800–2000 line architecture document covering:

- System overview and design principles
- ASCII diagrams of components, workflows, and state machines
- Tool taxonomy with YAML definitions and invocation examples
- Memory architecture (working / session / long-term)
- Routing and decision logic
- Quality gates and evaluation strategy
- Prompting strategies with example prompts
- Full Claude API implementation with working code
- Tracing and observability approach
- Scaling considerations and extension patterns

## How to use

1. Open [`architecture_generator_prompt.md`](architecture_generator_prompt.md)
2. Copy the prompt inside the `## THE PROMPT` section
3. Replace `[YOUR INPUT HERE]` with a description of your agent
4. Paste into Claude (Claude.ai, API, or Claude Code)
5. Answer the clarifying questions Claude asks (up to 10, only what's relevant)
6. Receive your complete architecture document

## What to put in `[YOUR INPUT HERE]`

Describe your agent in plain language. Include:

- **What it does** — the core task or workflow
- **Inputs** — what the agent receives (text, files, URLs, structured data)
- **Outputs** — what it produces and in what format
- **Any structure ideas** — tools you're imagining, steps you have in mind

The more context you give, the more specific the output. Vague inputs produce generic architectures; concrete inputs produce actionable ones.

### Example

```
I want to build an agent that monitors my inbox for supplier invoices,
extracts line items, checks them against purchase orders in a Google Sheet,
and flags discrepancies for human review.

Inputs: Gmail (via MCP), Google Sheets (via MCP)
Outputs: Slack message with flagged discrepancies, updated Sheet column
Human review needed before any payment approval
```

## Tips

- **Mention constraints early** — budget sensitivity, latency requirements, existing systems to integrate with
- **State what should never happen** — helps Claude design the right guardrails
- **Say your technical level** — Claude calibrates implementation detail accordingly
- **"Like X but for Y"** — analogies help Claude understand the pattern you're after

## Output

Save the generated document as `[AGENT_NAME]_AGENTIC_ARCHITECTURE.md` alongside your project. It serves as requirements doc, system design, and implementation reference in one.
