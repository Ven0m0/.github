---
name: linting-llm-configs
description: Optimizes and validates AI agent configuration files (CLAUDE.md, skill files, hooks, MCP) using claudelint and agnix. Use when asked to lint agent configs.
---

# Linting LLM Configs

Optimizes and validates AI assistant configurations across multiple platforms.

<overview>
Use this skill for project-wide AI guidance files (`CLAUDE.md`, skills, prompts, MCP config) and for agent-config linting with `claudelint` or `agnix`.
</overview>

<instructions>

## Validation Tools

### Which tool to use?

| File / config                        | Prefer                 | Why                                    |
| ------------------------------------ | ---------------------- | -------------------------------------- |
| `CLAUDE.md`, Claude Code skills      | `claudelint`           | Deep Claude Code validation/formatting |
| `SKILL.md`, `AGENTS.md`, Copilot/MCP | `agnix`                | Cross-tool rule coverage               |
| Mixed Claude Code repo               | `claudelint` + `agnix` | Structure + ecosystem coverage         |

### claudelint workflow
```bash
claudelint init
claudelint check-all
```

### agnix workflow
```bash
agnix .
agnix --fix-safe .
```

## Install

bun install -g claude-code-lint
bun install -g agnix

</instructions>

## References

- [Validation guide](references/guide.md)
