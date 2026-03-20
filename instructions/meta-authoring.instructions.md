---
applyTo: "**/{*.agent.md,SKILL.md,*.instructions.md,*.prompt.md}"
---

# Meta-Authoring: Agents, Skills, Instructions, Prompts

<HighLevelDetails>

- **Agents**: `.github/agents/` or `agents/` | Docs: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- **Skills**: `skills/<name>/` or `.github/skills/<name>/` | Task-specific workflows, portable across VS Code/Copilot
- **Instructions**: `instructions/` | Coding standards, applyTo glob
- **Prompts**: `.github/prompts/` | `.prompt.md` extension

</HighLevelDetails>

## Agents (*.agent.md)

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Yes | 50-150 chars, actionable |
| `name` | No | Defaults to filename |
| `tools` | No | Omit = all. Principle of least privilege |
| `model` | Optional | claude-4-6-sonnet/opus/haiku-latest. Ignored on GitHub.com |

**Structure**: Identity -> Responsibilities -> Workflow -> Triggers. Imperative mood.

## Skills (SKILL.md)

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Kebab-case, max 64 chars, no `claude`/`anthropic` |
| `description` | Yes | WHAT + WHEN + Keywords. Primary discovery mechanism |

**Sections**: When to Use, Workflows, Examples. Keep under 500 lines; use `modules/` for depth.

## Instructions (*.instructions.md)

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Yes | 1-500 chars |
| `applyTo` | Yes | Glob: `**/*.py`, `**` |

**Content**: Concrete examples, tables over prose. XML tags: `<Goals>`, `<Standards>`, `<Limitations>`.

## Prompts (*.prompt.md)

| Field | Required | Notes |
|-------|----------|-------|
| `description` | Yes | One sentence, actionable |
| `mode` | Yes | `ask` \| `edit` \| `agent` |
| `tools` | Recommended | Minimal set |

**Structure**: Mission -> Scope -> Workflow -> Output. Inputs: `${input:name[:placeholder]}`.

<Standards>

- Imperative mood; specific and actionable
- Tables for options, constraints, commands
- No vague terms ("should", "might")
- Least-privilege tools

</Standards>

<Limitations>

- No hardcoded credentials
- No excessive tool access
- No contradictory advice across files

</Limitations>
