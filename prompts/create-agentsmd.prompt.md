---
description: "Generate AGENTS.md for a repository"
mode: agent
tools: ["read", "edit", "search", "execute"]
---

# Create AGENTS.md

Generate a complete AGENTS.md at repository root following https://agents.md/

AGENTS.md is "README for agents" - provides AI coding agents with actionable technical context.

## Required Sections

```markdown
# AGENTS.md

## Project Overview

[Description, purpose, key technologies]

## Setup Commands

- Install: `[pkg mgr] install`
- Build: `[cmd]`

## Development Workflow

- Start dev: `[cmd]`
- Hot reload: `[cmd]`

## Testing

- Run all: `[cmd]`
- Coverage: `[cmd]`

## Code Style

- Lint: `[cmd]`
- Format: `[cmd]`

## Build and Deployment

- Build: `[cmd]`
- Deploy: `[cmd]`

## PR Guidelines

- Title format, required checks
```

## Process

1. **Analyze**: Languages, frameworks, build tools, testing, architecture
2. **Extract**: Commands from package.json, Makefile, CI configs
3. **Write**: Exact, executable commands agents can run directly
4. **Validate**: Test all commands work
