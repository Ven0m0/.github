# Instruction Modules Index

Navigation guide for the Ven0m0 `.github` repository's instruction modules.

## Language Standards

| Module | Scope | File Types |
|--------|-------|-----------|
| **bash** | Bash/Shell scripting standards | `*.sh`, `*.bash` |
| **python** | Python coding standards | `*.py` |
| **javascript** | JavaScript/TypeScript standards | `*.js`, `*.ts`, `*.tsx`, `*.jsx` |
| **typescript** | TypeScript strict standards | `*.ts`, `*.tsx` |
| **rust** | Rust coding standards | `*.rs` |
| **go** | Go 1.23+ standards | `*.go` |
| **java** | Java 21 LTS standards | `*.java` |
| **kotlin** | Kotlin 2.0+ standards | `*.kt`, `*.kts` |
| **cpp** | C++23/20 standards | `*.cpp`, `*.hpp`, `*.h`, `*.cc` |
| **csharp** | C# 12/.NET 8 standards | `*.cs`, `*.csproj` |
| **swift** | Swift 6+ standards | `*.swift` |
| **ruby** | Ruby 3.3+ standards | `*.rb`, `Gemfile` |
| **php** | PHP 8.3+ standards | `*.php`, `composer.json` |
| **scala** | Scala 3.4+ standards | `*.scala`, `*.sc` |
| **elixir** | Elixir 1.17+ standards | `*.ex`, `*.exs` |
| **flutter** | Flutter/Dart standards | `*.dart`, `pubspec.yaml` |
| **r** | R 4.4+ standards | `*.R`, `*.Rmd` |
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
| **file-reading-optimization** | Tiered file reading strategy, token budget awareness |

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
| TypeScript | `typescript` | `javascript` |
| Rust | `rust` | `quality-standards` |
| Go | `go` | `quality-standards` |
| Java | `java` | `quality-standards` |
| Kotlin | `kotlin` | `quality-standards` |
| C++ | `cpp` | `quality-standards` |
| C# | `csharp` | `quality-standards` |
| Swift | `swift` | `quality-standards` |
| Ruby | `ruby` | `quality-standards` |
| PHP | `php` | `quality-standards` |
| Scala | `scala` | `quality-standards` |
| Elixir | `elixir` | `quality-standards` |
| Flutter/Dart | `flutter` | `quality-standards` |
| R | `r` | `quality-standards` |
| Bash scripts | `bash` | - |
| PowerShell | `powershell` | - |
| Makefiles | `makefile` | - |
| GitHub Actions | `cicd-standards` | - |
| Code review | `quality-standards` | Language-specific module |
| Agent/skill/instruction authoring | `meta-authoring` | `ai-tuning` |
| Token efficiency | `file-reading-optimization` | `ai-tuning` |

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

*Last Updated: March 2026*
