# Agentic Architecture Generator Prompt

**Purpose**: Use this prompt with Claude to generate a comprehensive agentic system architecture document for any workflow you want to build.

**How to Use**:
1. Copy the prompt below
2. Replace `[YOUR INPUT HERE]` with your agent description
3. Paste into Claude (API, Console, or Claude.ai)
4. Answer the clarifying questions Claude asks
5. Receive your complete architecture document

---

## THE PROMPT

```
You are an expert AI systems architect specializing in agentic workflows, following Anthropic's best practices for building effective agents. Your task is to help me design and document a complete agentic system architecture.

## MY AGENT IDEA

[YOUR INPUT HERE - Describe what you want the agent to do, potential inputs, outputs, and any structural ideas you have]

---

## YOUR TASK

Generate a comprehensive agentic architecture document for my use case. This document should serve as:
- Requirements document
- System architecture document
- Workflow specification
- Technical implementation guide

**IMPORTANT**: Before generating the full document, you MUST ask me clarifying questions to ensure the architecture fits my actual needs. Ask up to 10 questions, but only ask what's necessary - skip questions where the answer is obvious from my input.

---

## PHASE 1: DISCOVERY QUESTIONS

Ask me clarifying questions from these categories. Be selective - only ask what you genuinely need to know:

### Problem Understanding
- What problem does this agent solve that couldn't be solved with a simple prompt?
- Who is the user? What's their technical level?
- What does success look like? How will we measure it?

### Inputs & Outputs
- What are ALL possible input types (text, files, URLs, structured data)?
- What are the expected outputs? In what format?
- Are there intermediate outputs users might want to see/approve?

### Data & Memory
- What data does the agent need access to? Where does it live?
- Does the agent need to remember things across sessions?
- Is there existing data that needs to be indexed/retrieved?

### Workflow & Decisions
- Is this a single-shot task or a multi-step workflow?
- Are there decision points where different paths could be taken?
- Should the user be involved at any checkpoints (human-in-the-loop)?

### Quality & Safety
- What could go wrong? What are the failure modes?
- Are there things the agent should NEVER do?
- How will we validate the outputs are correct?

### Technical Constraints
- What's the token budget concern (cost-sensitive or quality-first)?
- Does this need to integrate with external systems/APIs?
- What's the latency requirement (real-time vs batch)?

### Scale & Evolution
- Single user or multi-user?
- Will this grow over time? How?
- What features might be added later?

Present questions conversationally, grouped logically. Wait for my answers before proceeding.

---

## PHASE 2: ARCHITECTURE DOCUMENT GENERATION

After I answer your questions, generate a complete architecture document with this EXACT structure:

```markdown
# [Agent Name]: Agentic System Architecture

**A comprehensive breakdown of [Agent Name] as an LLM-powered agent system**

*Document Type: Requirements, System Architecture, Workflow, and Technical Reference*
*Version: 1.0 | [Date]*

---

## Table of Contents
1. Executive Summary
2. System Philosophy & Design Principles
3. Agentic Architecture Overview
4. Tools & Actions
5. Memory & State Management
6. Retrieval Architecture (if applicable)
7. Routing & Decision Logic
8. Quality Gates & Evaluations
9. Prompting Strategies
10. Data Layer & Storage
11. Tracing & Observability
12. Implementation with Claude API
13. Advanced Patterns & Extensions
14. Appendix

---

## 1. Executive Summary

### What is [Agent Name]?
[2-3 paragraph description of what the agent does and why it matters]

### Why an Agentic Approach?
[Explain why this needs to be an agent vs simple prompting]
- Problem 1 that agents solve
- Problem 2 that agents solve
- Problem 3 that agents solve

### Key Metrics
| Metric | Target Value |
|--------|--------------|
| [Metric 1] | [Target] |
| [Metric 2] | [Target] |
| ... | ... |

---

## 2. System Philosophy & Design Principles

### Core Design Principles

#### 2.1 [Principle 1 Name]
```
PRINCIPLE: [One-line statement]

IMPLEMENTATION:
- How this is enforced
- Specific mechanisms
- Examples
```

#### 2.2 [Principle 2 Name]
[Same format...]

[Continue for 4-6 principles relevant to this agent]

---

## 3. Agentic Architecture Overview

### 3.1 System Components

[ASCII diagram showing all major components and their relationships]

```
┌─────────────────────────────────────────────────────────────────────┐
│                        [AGENT NAME] SYSTEM                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [Component diagram with boxes and arrows]                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Agent Type Classification

Following Anthropic's agent patterns, this is a [TYPE] agent:

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| [Pattern 1] | [Description] | [How used] |
| [Pattern 2] | [Description] | [How used] |

### 3.3 Agent Workflow (Agentic Loop)

[ASCII diagram showing the main workflow loop with phases and gates]

---

## 4. Tools & Actions

### 4.1 Tool Taxonomy

```yaml
tools:
  # Category 1
  - name: tool_name
    description: What it does
    parameters:
      - param1: type
      - param2: type
    returns: return_type

  # Category 2
  [Continue for all tools...]
```

### 4.2 Tool Categories

| Category | Tools | Purpose |
|----------|-------|---------|
| [Category 1] | [tool1, tool2] | [Purpose] |
| [Category 2] | [tool3, tool4] | [Purpose] |

### 4.3 Tool Invocation Examples

[Show concrete examples of how tools are called]

---

## 5. Memory & State Management

### 5.1 Memory Types

[ASCII diagram showing memory architecture]

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MEMORY ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    LONG-TERM MEMORY                          │   │
│  │  [What persists across sessions]                             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    SESSION MEMORY                            │   │
│  │  [What persists within a session/task]                       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    WORKING MEMORY                            │   │
│  │  [What's in the context window now]                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.2 Memory Operations

| Operation | Memory Type | Example |
|-----------|-------------|---------|
| [Op 1] | [Type] | [Example] |

### 5.3 State Transitions

[State machine diagram for the workflow]

---

## 6. Retrieval Architecture

[If the agent needs RAG - otherwise note "Not applicable for this agent"]

### 6.1 Why Retrieval?
[Explain why retrieval is needed]

### 6.2 Retrieval Flow
[ASCII diagram of retrieval pipeline]

### 6.3 Indexing Strategy
[How data is indexed for retrieval]

### 6.4 Query Strategy
[How queries are constructed and executed]

### 6.5 Retrieval Implementation

```python
# Code example for retrieval
```

---

## 7. Routing & Decision Logic

### 7.1 Router Architecture

[ASCII diagram showing routing flow]

### 7.2 Decision Trees

[Show key decision trees in code or diagram form]

```python
def route_request(input):
    if condition1:
        return handler1
    elif condition2:
        return handler2
    ...
```

### 7.3 Phase Routing

[If multi-phase, show how phases transition]

---

## 8. Quality Gates & Evaluations

### 8.1 Gate Architecture

[ASCII diagram showing all gates in the workflow]

### 8.2 Gate Definitions

#### Gate 1: [Name]
```
Location: After [phase/step]

Checks:
□ Check 1
□ Check 2
□ Check 3

On Fail: [What happens]
```

[Continue for all gates...]

### 8.3 Evaluation Types

| Type | Purpose | Implementation |
|------|---------|----------------|
| Validation | Pass/fail checks | [How] |
| Scoring | Quality assessment | [How] |
| Comparison | A/B evaluation | [How] |

### 8.4 Implementing Gates

```python
# Code example for gate implementation
```

---

## 9. Prompting Strategies

### 9.1 Prompt Architecture

[List all prompts and their purposes]

```
prompts/
├── prompt1.md    # Purpose
├── prompt2.md    # Purpose
└── prompt3.md    # Purpose
```

### 9.2 Prompt Structure Pattern

[Show the consistent structure used across prompts]

### 9.3 Key Prompting Techniques

#### 9.3.1 [Technique 1]
[Explain with examples]

#### 9.3.2 [Technique 2]
[Explain with examples]

### 9.4 Example Prompts

[Provide 1-2 complete example prompts]

---

## 10. Data Layer & Storage

### 10.1 Storage Architecture

[ASCII diagram of storage structure]

### 10.2 Data Schemas

[Define schemas for key data structures]

### 10.3 File/Database Structure

```
project/
├── folder1/
│   ├── file1.ext    # Purpose
│   └── file2.ext    # Purpose
├── folder2/
...
```

---

## 11. Tracing & Observability

### 11.1 Tracing Approach

[How tracing is implemented]

### 11.2 What to Track

| Dimension | What to Track | How |
|-----------|---------------|-----|
| Inputs | [What] | [How] |
| Decisions | [What] | [How] |
| Outputs | [What] | [How] |
| Quality | [What] | [How] |

### 11.3 Key Metrics

| Metric | Purpose | Target |
|--------|---------|--------|
| [Metric 1] | [Why] | [Value] |

---

## 12. Implementation with Claude API

### 12.1 Architecture Pattern

[Recommend orchestrator vs chaining vs multi-agent]

### 12.2 Core Implementation

```python
# Complete working example of the main agent loop
```

### 12.3 Tool Definitions

```python
# Complete tool definitions for Claude API
TOOLS = [
    {
        "name": "...",
        "description": "...",
        "input_schema": {...}
    }
]
```

### 12.4 Full Working Example

```python
# End-to-end implementation example
```

---

## 13. Advanced Patterns & Extensions

### 13.1 Potential Enhancements

[List 3-5 future enhancements with implementation sketches]

### 13.2 Scaling Considerations

| Scale | Implementation | Notes |
|-------|---------------|-------|
| Single user | [Approach] | [Notes] |
| Team | [Approach] | [Notes] |
| Enterprise | [Approach] | [Notes] |

### 13.3 Integration Possibilities

[List potential integrations with external systems]

---

## 14. Appendix

### 14.1 Complete File Structure

[Full directory tree]

### 14.2 Configuration Reference

[All configuration options]

### 14.3 Quick Reference

[Cheat sheet for common operations]

---

## Summary: Key Takeaways

[5-7 bullet points summarizing the most important architectural decisions and why they matter]

---

*Document generated by Claude | [Date]*
```

---

## GENERATION RULES

1. **Be specific, not generic**: Every section should contain concrete details for THIS agent, not placeholder text
2. **Include working code**: All code examples should be complete and functional
3. **Use ASCII diagrams**: Visualize architecture, workflows, and state machines
4. **Maintain consistency**: Use the same terminology throughout
5. **Justify decisions**: Explain WHY each architectural choice was made
6. **Consider failure modes**: Address what could go wrong in each section
7. **Be practical**: Focus on what's needed for v1, mention extensions for later
8. **Match complexity to problem**: Simple agents get simpler docs, complex get detailed

---

## OUTPUT FORMAT

After asking questions and receiving answers:
1. Summarize my requirements back to me (1 paragraph)
2. Propose the high-level architecture (bullet points)
3. Ask if I want to proceed or adjust
4. Generate the complete document

The final document should be 800-2000 lines depending on complexity, saved as `[AGENT_NAME]_AGENTIC_ARCHITECTURE.md`
```

---

## EXAMPLE INPUT

Here's an example of how to fill in `[YOUR INPUT HERE]`:

```
I want to build an agent that helps me manage my personal knowledge base.

**What it does**:
- Ingests content from various sources (articles, PDFs, YouTube transcripts, my notes)
- Extracts key insights and tags them
- Answers questions by retrieving relevant knowledge
- Generates weekly summaries of what I've learned
- Suggests connections between ideas

**Inputs**:
- URLs to articles/videos
- PDF files
- Raw text notes
- Questions in natural language

**Outputs**:
- Structured knowledge entries
- Answers with citations
- Weekly digest emails
- Knowledge graph visualizations

**Structure ideas**:
- Maybe use embeddings for semantic search
- Want human approval before adding to permanent knowledge base
- Should work with Obsidian markdown files
```

---

## TIPS FOR BEST RESULTS

1. **Be detailed in your input**: The more context you provide, the better the architecture
2. **Mention constraints early**: Budget, latency, existing systems
3. **Include examples**: "Like X but for Y" helps Claude understand
4. **State non-obvious requirements**: Things that might not be assumed
5. **Share your technical level**: Helps Claude calibrate implementation detail
