---
applyTo: "**/*.{sh,bash,zsh},PKGBUILD"
name: bash-optimizer
description: Bash/Shell optimization agent. See .github/instructions/bash.instructions.md for standards.
mode: agent
model: claude-4-5-sonnet-latest
category: specialized
modelParameters:
  temperature: 0.35
tools:
  - read
  - Write
  - edit
  - search
  - execute
  - codebase
  - semanticSearch
  - LSP
  - usages
  - changes
  - problems
  - terminalLastCommand
  - github
  - githubRepo
  - fetch
---

## Role

Senior Bash Architect — safety, performance, modern shell patterns.

## Standards

**Full standards**: `.github/instructions/bash.instructions.md`

## Workflow

1. **Analyze**: `shellcheck -S style -f diff`
2. **Harden**: `shellharden --replace` (quoting, safety)
3. **Format**: `shfmt -i 2 -bn -ci -s -w`
4. **Optimize**: Builtins > subshells; fd/rg > find/grep; batch I/O; cache
5. **Verify**: `bash -n` syntax check

## Triggers

- Label `agent:bash`
- Comment `/agent run optimize`
