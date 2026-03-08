---
description: 'Write and optimize Bash/Shell scripts following project standards for Arch, Debian, and Termux platforms'
mode: agent
applyTo: "**/*.sh"
---

# Bash Agent Prompt

## Context

- **Target**: Bash/Shell
- **Standards**: See `instructions/bash.instructions.md` for complete rules
- **Platforms**: Arch, Debian, Termux

## Task: ${TASK_NAME}

- **Input**: Files:${FILES}, Trigger:${TRIGGER}, Scope:${SCOPE}

## Execution Steps

Follow the workflow defined in `instructions/bash.instructions.md`:

1. **Find**: `fd -e sh -e bash -t f -H -E .git ${scope}`
2. **Lint**: `shellcheck --severity=style --format=diff ${files}`
3. **Format**: `shfmt -i 2 -bn -s -ln bash -w ${files}`
4. **Validate**: Shebang, strict mode, error handling
5. **Optimize**: Use builtins, modern tools (fd, rg, jaq), minimize forks
6. **Report**: Changes count, risk level (L/M/H)

## Success Criteria

- Zero lint warnings, consistent formatting, no breaking changes, tests pass
- PR with atomic commits: `[agent] task:...`
