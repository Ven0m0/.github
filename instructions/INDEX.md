# Instruction Modules Index

Navigation guide for the Ven0m0 `.github` repository's instruction modules.

## Language Standards

| Module | Scope | File Types |
|--------|-------|-----------|
| **bash** | Bash/Shell scripting standards | `*.sh`, `*.bash` |
| **python** | Python coding standards | `*.py` |
| **javascript** | JavaScript/TypeScript standards | `*.js`, `*.ts`, `*.tsx`, `*.jsx` |
| **rust** | Rust coding standards | `*.rs` |
| **powershell** | PowerShell scripting | `*.ps1`, `*.psm1`, `*.psd1` |
| **cmd** | CMD/Batch scripting | `*.bat`, `*.cmd` |
| **autohotkey** | AutoHotkey v2 scripting | `*.ahk` |

## Build & CI/CD

| Module | Scope | File Types |
|--------|-------|-----------|
| **makefile** | Makefile and cross-shell patterns | `Makefile`, `*.mk`, `*.make` |
| **cicd-standards** | GitHub Actions, CI/CD patterns | `.github/workflows/*.yml` |

## Quality & Review

| Module | Scope |
|--------|-------|
| **quality-standards** | Code review, performance optimization |
| **html-css-style-color-guide** | Color and styling rules |

## AI & Tooling

| Module | Scope |
|--------|-------|
| **meta-authoring** | Agents, skills, instructions, prompts |
| **ai-tuning** | AI assistant configs, guard rails, output compression |

## Documentation & Process

| Module | Scope |
|--------|-------|
| **markdown** | Documentation standards |
| **memory-bank** | Session context persistence |
| **update-docs-on-code-change** | Doc sync with code changes |

## Platform-Specific

| Module | Scope |
|--------|-------|
| **arch-linux** | Arch Linux administration |
| **python-mcp-server** | Python MCP server development |

## Navigation by File Type

| Working On | Primary | Secondary |
|------------|---------|-----------|
| Python | `python` | `quality-standards` |
| JS/TS | `javascript` | `quality-standards` |
| Rust | `rust` | `quality-standards` |
| Bash scripts | `bash` | - |
| PowerShell | `powershell` | - |
| Makefiles | `makefile` | - |
| GitHub Actions | `cicd-standards` | - |
| Code review | `quality-standards` | Language-specific module |
| Agent/skill/instruction authoring | `meta-authoring` | `ai-tuning` |

## XML Tag Convention

| Tag | Purpose |
|-----|---------|
| `<Goals>` | What the instructions aim to achieve |
| `<Standards>` | Rules and conventions to follow |
| `<Limitations>` | Forbidden patterns |
| `<Security>` | Security requirements |
| `<WhatToAdd>` | What to include in generated code |
| `<HighLevelDetails>` | Architecture/context overview |

---

*Last Updated: February 2026*
