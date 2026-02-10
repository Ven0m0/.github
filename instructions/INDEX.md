# Instruction Modules Index

Navigation guide for the Ven0m0 `.github` repository's consolidated instruction modules.

## Module Overview

| Module | Scope | File Types |
|--------|-------|-----------|
| **lang-standards** | Python, JS/TS, Rust coding standards | `*.py`, `*.js`, `*.ts`, `*.tsx`, `*.jsx`, `*.rs` |
| **shell-standards** | Makefile, cross-shell patterns | `Makefile`, `*.mk`, `*.make` |
| **bash** | Bash scripting standards | `*.sh`, `*.bash` |
| **powershell** | PowerShell scripting | `*.ps1`, `*.psm1`, `*.psd1` |
| **cmd** | CMD/Batch scripting | `*.bat`, `*.cmd` |
| **quality-standards** | Code review, performance optimization | All code files |
| **cicd-standards** | GitHub Actions, CI/CD patterns | `.github/workflows/*.yml` |
| **github-actions-ci-cd** | Advanced CI/CD best practices | `.github/workflows/*.yml` |

## Domain-Specific Modules

| Module | Scope |
|--------|-------|
| **agents** | Creating custom agent files |
| **agent-skills** | Creating Agent Skills |
| **ai-tuning** | Optimizing AI assistant configs |
| **instructions** | Creating instruction files |
| **prompt** | Creating prompt files |
| **markdown** | Documentation standards |
| **token-efficient** | Compressed output mode |
| **memory-bank** | Session context persistence |
| **update-docs-on-code-change** | Doc sync with code changes |
| **taming-copilot** | Copilot guard rails |
| **html-css-style-color-guide** | Color and styling rules |
| **arch-linux** | Arch Linux administration |
| **autohotkey** | AutoHotkey v2 scripting |
| **python-mcp-server** | Python MCP server development |
| **shell** | General shell scripting |

## Navigation by File Type

| Working On | Primary | Secondary |
|------------|---------|-----------|
| Python | `lang-standards` | `quality-standards` |
| JS/TS | `lang-standards` | `quality-standards` |
| Rust | `lang-standards` | `quality-standards` |
| Bash scripts | `bash` | `shell` |
| PowerShell | `powershell` | - |
| Makefiles | `shell-standards` | - |
| GitHub Actions | `cicd-standards` | `github-actions-ci-cd` |
| Code review | `quality-standards` | Language-specific module |
| Agent development | `agents` | `agent-skills` |
| Instruction authoring | `instructions` | `ai-tuning` |

## XML Tag Convention

All instruction files use semantic XML tags for Copilot to parse structured content:

| Tag | Purpose |
|-----|---------|
| `<Goals>` | What the instructions aim to achieve |
| `<Standards>` | Rules and conventions to follow |
| `<Limitations>` | What to avoid, forbidden patterns |
| `<Security>` | Security requirements |
| `<WhatToAdd>` | What to include in generated code |
| `<HighLevelDetails>` | Architecture/context overview |

## Cross-Module Principles

These appear across multiple modules for consistency:
1. Type safety (lang-standards: Python, TypeScript, Rust)
2. Fail fast (lang-standards, bash, shell-standards)
3. Security by default (lang-standards, bash, cicd-standards)
4. Testing discipline (lang-standards, quality-standards)
5. Performance awareness (lang-standards, quality-standards)

---

*Last Updated: February 2026*
