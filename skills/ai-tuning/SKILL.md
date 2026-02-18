---
name: ai-tuning
description: Optimize AI assistant configurations (CLAUDE.md, copilot-instructions.md, AGENTS.md, MCP). Deduplicate memory files. Use when asked to "improve CLAUDE.md", "better copilot instructions", "tune AI", "condense CLAUDE.md", or "optimize prompts".
user-invocable: true
disable-model-invocation: false
---

# AI Tuning Skill

Optimize AI assistant configurations. Standards: `instructions/ai-tuning.instructions.md`

## Triggers

| Phrase | Target |
|--------|--------|
| "improve CLAUDE.md" | CLAUDE.md |
| "better copilot instructions" | copilot-instructions.md |
| "condense CLAUDE.md", "deduplicate memory" | CLAUDE.md hierarchy |
| "tune AI" | All configs |
| "optimize prompts" | Prompts, AGENTS.md |
| "add MCP servers" | .vscode/mcp.json |

## Workflow

1. **Analyze**: Read existing AI config files
2. **Identify gaps**: Missing context, vague instructions, outdated commands, duplication
3. **Optimize**: Dense over verbose; examples over descriptions; tables over prose
4. **Validate**: All commands exact and executable

## Condensation (CLAUDE.md Deduplication)

| Phase | Action |
|-------|--------|
| Discovery | Find CLAUDE.md files; detect intra-file and cross-file duplication |
| Analysis | Identify misplaced content (subdir with project-wide content) |
| Present | Show duplicates, affected files, proposed consolidation; wait for approval |
| Implement | Remove duplicates, move misplaced, merge similar |

**Hierarchy**: `./CLAUDE.md` (project) > `./.claude/rules/*.md` (topic) > `./subdir/CLAUDE.md` (dir-only)

## Copilot Optimization Rules

| Principle | Apply |
|-----------|-------|
| Context density | One line: `Python 3.12 \| ruff \| pytest` not paragraphs |
| Example-driven | Code block with `...` over "use type annotations" |
| Constraint tables | `\| Action \| Command \|` for build/test/lint |
| Guard rails | User directives > internal knowledge; code on request only |
