---
description: 'Standards for optimizing AI assistant configurations (CLAUDE.md, copilot-instructions.md, MCP, AGENTS.md)'
applyTo: '**/CLAUDE.md,**/copilot-instructions.md,**/.vscode/mcp.json,**/AGENTS.md'
---

# AI Tuning Instructions

<Goals>

1. Be specific: vague instructions produce vague results
2. Show examples: concrete code > descriptions
3. State constraints: explicitly list what NOT to do
4. Organize hierarchically: general to specific
5. Include commands: build/test/lint for quick reference

</Goals>

## copilot-instructions.md Structure

```markdown
# GitHub Copilot Instructions
## Project Context
[Brief description, tech stack, key dependencies]
## Code Generation Guidelines
### [Language] Patterns
[Conventions, type annotations, imports, error handling]
### Examples
[GOOD/AVOID pattern pairs]
## Commands
[build, test, lint commands]
```

## CLAUDE.md Structure

```markdown
# CLAUDE.md
## Project Overview
[What it does, architecture, technologies]
## Build Commands
[install, test, lint, type check - exact commands]
## Code Style Requirements
[Formatter, linter config, key rules with examples]
## Architecture Guidelines
[Key patterns, layer responsibilities, dependency rules]
```

## AGENTS.md Structure

Agent-focused technical instructions. Complements README.md with actionable context.

Essential sections: Project Overview, Setup Commands, Development Workflow, Testing Instructions, Code Style, Build/Deployment, PR Guidelines, Notes/Gotchas

<Standards>

**Key Principles**:
1. Actionable commands agents can execute
2. Test all commands to ensure they work
3. Stay current as project evolves
4. Focus on what agents need, not general info

</Standards>

## Optimization Techniques

### Context Density
```markdown
# Verbose (waste):
"This project uses Python 3.12. We use ruff for linting. Testing is done with pytest."

# Dense (good):
"Python 3.12 | ruff (lint+format) | pytest"
```

### Example-Driven
```markdown
# Verbose: "Use type annotations on all functions."
# Dense: "Type annotations required:"
def process(items: list[str], limit: int = 10) -> dict[str, int]: ...
```

### Constraint Tables
| Action | Command |
|--------|---------|
| Test | `uv run pytest` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` |
| Type check | `uv run pyright` |

## MCP Configuration

```json
{
  "mcpServers": {
    "context7": { "command": "npx", "args": ["-y", "@context7/mcp-server"] },
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"] }
  }
}
```

<Limitations>

- No verbose prose when tables or lists suffice
- No duplicating info available in other instruction files
- No outdated tool versions or commands
- No vague guidance ("should", "might", "possibly")

</Limitations>
