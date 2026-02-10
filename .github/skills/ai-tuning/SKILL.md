---
name: ai-tuning
description: Optimize AI assistant configurations (CLAUDE.md, copilot-instructions.md, AGENTS.md, MCP). Use when asked to "improve CLAUDE.md", "better copilot instructions", "tune AI", or "optimize prompts".
user-invocable: true
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# AI Tuning Skill

Optimize AI assistant configurations for maximum effectiveness.

Standards: See `instructions/ai-tuning.instructions.md`

## Triggers

- "improve my CLAUDE.md"
- "better copilot instructions"
- "tune AI for this project"
- "add MCP servers"

## Workflow

1. **Analyze**: Read existing AI config files
2. **Identify gaps**: Missing context, vague instructions, outdated commands
3. **Optimize**: Dense over verbose, examples over descriptions, tables over prose
4. **Validate**: Ensure all commands are exact and executable
