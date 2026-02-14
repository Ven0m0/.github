---
description: 'Guidelines for creating custom agent files for GitHub Copilot'
applyTo: '**/*.agent.md'
excludeAgent: "code-review"
---

# Custom Agent File Guidelines

<HighLevelDetails>

- Format: Markdown with YAML frontmatter
- Naming: lowercase with hyphens (e.g., `test-specialist.agent.md`)
- Location: `.github/agents/` (repo) or `agents/` (org/enterprise)
- Docs: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents

</HighLevelDetails>

## Required Frontmatter

```yaml
---
description: 'Brief description of agent purpose and capabilities'
name: 'Agent Display Name'
tools: ['read', 'edit', 'search']
model: 'Claude Sonnet 4.5'
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Yes | Single-quoted, 50-150 chars, actionable |
| `name` | No | Defaults to filename without extension |
| `tools` | No | Omit = all tools. `[]` = none |
| `model` | Recommended | `Claude Sonnet 4.5`, `gpt-4o`, etc. |
| `target` | No | `vscode` or `github-copilot` |
| `infer` | No | `false` = require manual selection |
| `handoffs` | No | VS Code 1.106+ only |

## Tool Configuration

### Standard Tool Aliases

| Alias | Alternatives | Description |
|-------|-------------|-------------|
| `execute` | shell, Bash, powershell | Shell execution |
| `read` | Read, NotebookRead, view | File reading |
| `edit` | Edit, MultiEdit, Write | File editing |
| `search` | Grep, Glob | Code search |
| `agent` | custom-agent, Task | Invoke other agents |
| `web` | WebSearch, WebFetch | Web access |

### MCP Server Tools
```yaml
tools: ['github/*']           # All GitHub tools
tools: ['playwright/navigate'] # Specific Playwright tool
```

<Standards>

**Principle of Least Privilege**: Only enable tools necessary for the agent's purpose
**Prompt Structure**:
1. Agent identity and role
2. Core responsibilities
3. Approach and methodology
4. Guidelines and constraints
5. Output expectations

**Writing Style**: Imperative mood ("Analyze", "Generate"), specific and actionable, structured with headers/bullets

</Standards>

## Handoffs (VS Code Only)

```yaml
handoffs:
  - label: Start Implementation
    agent: implementation
    prompt: 'Implement the plan outlined above.'
    send: false
```

| Property | Required | Description |
|----------|----------|-------------|
| `label` | Yes | Button text ("Start Implementation", not "Next") |
| `agent` | Yes | Target agent identifier |
| `prompt` | No | Pre-filled text for target agent |
| `send` | No | `true` = auto-submit (default: `false`) |

Limit to 2-3 relevant handoffs per agent. Ensure target agents exist.

## Sub-Agent Orchestration

Enable with `tools: ['read', 'edit', 'search', 'agent']`. Sub-agents cannot access tools unavailable to parent.

```text
This phase must be performed as the agent "<NAME>" defined in "<SPEC_PATH>".
IMPORTANT:
- Read and apply the entire .agent.md spec.
- Work on "<WORK_UNIT>" with base path: "<BASE_PATH>".
- Return summary: actions taken, files modified, issues found.
```

<Limitations>

- Not suitable for large-scale data processing (100s+ files)
- Each sub-agent invocation adds latency
- Max 5-10 sequential orchestration steps
- Total agent content under 30,000 characters
- Filename: only `.`, `-`, `_`, `a-z`, `A-Z`, `0-9`
- Missing `description` field is the most common error
- Excessive tool access degrades performance

</Limitations>

## Common Patterns

| Pattern | Tools | Focus |
|---------|-------|-------|
| Testing Specialist | all | Test coverage, quality |
| Implementation Planner | read, search, edit | Technical plans, no code |
| Code Reviewer | read, search | Review, no modifications |
| Security Auditor | read, search, web | OWASP, vulnerability scanning |
