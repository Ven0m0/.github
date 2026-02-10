# Ven0m0 .github Repository Guide

Organization-wide default community health files, Copilot instructions, AI agents, and development standards for all Ven0m0 repositories.

## Directory Structure

```
.github/
  agents/            # 21 specialized AI agents
  skills/            # 11 reusable skill modules
  instructions/      # 21 Copilot instruction files
  hooks/             # Pre-commit hooks
  prompts/           # Reusable prompt templates
  .gemini/           # Google Gemini configuration
  .github/workflows/ # Reusable GitHub Actions workflows
  AGENTS.md          # This file
  CLAUDE.md          # Symlink to AGENTS.md
  copilot-instructions.md
```

## Agents

The `agents/` directory contains 21 specialized autonomous agents:

### Workflow Orchestration

| Agent | Purpose |
|-------|---------|
| `multi-agent-workflow.agent.md` | Comprehensive multi-agent workflow orchestrating planning, execution, refactoring, cleanup, and review phases |

### Planning & Architecture

| Agent | Purpose |
|-------|---------|
| `plan.agent.md` | Strategic planning and architecture (opus) |
| `implementation-plan.agent.md` | Structured implementation plans from research |
| `prd.agent.md` | Product Requirements Document generator |
| `task-researcher.agent.md` | Deep research for task planning |

### Code Optimization & Refactoring

| Agent | Purpose |
|-------|---------|
| `bash.agent.md` | Bash/Shell optimization (modular, references language-optimization skill) |
| `python.agent.md` | Python optimization (modular, references language-optimization skill) |
| `rust.agent.md` | Rust optimization (modular, references language-optimization skill) |
| `refactoring-expert.agent.md` | Code refactoring with TDD principles |

### Development & Engineering

| Agent | Purpose |
|-------|---------|
| `workflow-engineer.agent.md` | GitHub Actions and CI/CD |
| `github-issue-fixer.agent.md` | Issue triage and resolution |
| `python-mcp-expert.agent.md` | Python MCP server development (modular, references mcp-development skill) |
| `typescript-mcp-expert.agent.md` | TypeScript MCP server development (modular, references mcp-development skill) |

### Repository & Knowledge Management

| Agent | Purpose |
|-------|---------|
| `agents-maintainer.agent.md` | Agent ecosystem maintenance |
| `repo-index.agent.md` | Repository indexing and search |
| `profile-maintainer.agent.md` | GitHub profile README management |
| `janitor.agent.md` | Codebase cleanup and maintenance |

### Quality & Analysis

| Agent | Purpose |
|-------|---------|
| `critical-thinking.agent.md` | Deep analysis and questioning |
| `context7.agent.md` | Documentation-powered assistant |
| `copilot-tuner.agent.md` | Copilot instruction optimization |
| `prompt-engineer.agent.md` | Prompt analysis and optimization |
| `arch-linux-expert.agent.md` | Arch Linux specialist |

### Agent Metadata

```yaml
---
name: agent-name
description: Brief description
model: claude-4-5-[sonnet|opus]-latest
tools: [codebase, read, write, edit, search, ...]
---
```

- **Sonnet** (0.3-0.4 temp): Code optimization, bug fixes, safe refactoring
- **Opus** (0.6-0.7 temp): Planning, architecture, complex analysis

## Skills

The `skills/` directory contains 11 reusable knowledge modules:

| Skill | Purpose |
|-------|---------|
| `gh-cli/` | GitHub CLI reference |
| `agentic-eval/` | Agent output evaluation patterns |
| `prd/` | PRD best practices |
| `ai-tuning/` | AI instruction optimization |
| `refactor/` | Refactoring strategies |
| `workflow-development/` | GitHub Actions workflows |
| `codebase-cleanup/` | Code cleanup procedures |
| `condense/` | CLAUDE.md deduplication |
| `agent-patterns/` | Reusable agent workflow patterns and templates |
| `language-optimization/` | Common language optimization patterns (Bash, Python, Rust) |
| `mcp-development/` | Common MCP server development patterns (Python, TypeScript) |

## Instructions

Organized in `instructions/` - scoped by file type and domain. See `instructions/INDEX.md` for full navigation.

### Language Standards

| File | Applies To |
|------|------------|
| `bash.instructions.md` | `*.sh`, `*.bash` |
| `python.instructions.md` | `*.py` |
| `javascript.instructions.md` | `*.js`, `*.ts`, `*.tsx`, `*.jsx` |
| `rust.instructions.md` | `*.rs` |
| `powershell.instructions.md` | `*.ps1`, `*.psm1` |
| `cmd.instructions.md` | `*.bat`, `*.cmd` |
| `autohotkey.instructions.md` | `*.ahk` |

### Build, CI/CD & Quality

| File | Applies To |
|------|------------|
| `makefile.instructions.md` | `Makefile`, `*.mk` |
| `cicd-standards.instructions.md` | `.github/workflows/*.yml` |
| `quality-standards.instructions.md` | All code files |

### AI & Tooling

| File | Applies To |
|------|------------|
| `agents.instructions.md` | `*.agent.md` |
| `agent-skills.instructions.md` | `SKILL.md` |
| `ai-tuning.instructions.md` | `CLAUDE.md`, `copilot-instructions.md` |
| `instructions.instructions.md` | `*.instructions.md` |
| `prompt.instructions.md` | `*.prompt.md` |
| `token-efficient.instructions.md` | All files |

## Development Workflows

### Git Workflow

```bash
git checkout -b feature/description
# Make focused changes
git commit -m "feat: add new agent"
git push -u origin feature/description
gh pr create --title "Feature: ..." --body "..."
```

### Conventional Commits

Format: `<type>(<scope>): <subject>`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Reusable Workflows

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
```

Available: `comprehensive-lint.yml`, `bun.yml`, `uv-lock.yml`, `dependabot-automerge.yml`, `img-opt.yml`, `git-maintenance.yml`, `release.yml`, `security.yml`

## Key Conventions

### Code Standards

- **KISS**: Simple over clever, readability first
- **YAGNI**: Don't build before needed
- **DRY**: Extract repeated logic
- **Fail Fast**: Validate early, specific error messages
- **Security**: No secrets in code, validate at boundaries

### Tool Preferences

| Task | Preferred | Fallback |
|------|----------|----------|
| Search | `rg` | `grep` |
| Find Files | `fd` | `find` |
| JSON/YAML | `jq`/`yq` | - |
| Stream Edit | `sd` | `sed` |
| Download | `aria2c` | `curl` |
| Dev (JS) | `bun` | `npm` |
| Dev (Python) | `uv` | `pip` |
| Lint (Python) | `ruff` | `black` |

### Communication Style

- No emojis in code/docs unless requested
- No em dashes - use hyphens or words
- Clear and direct, no ambiguous language
- Review first, then propose changes

## Extending This Repository

### Adding a New Agent

1. Create `agents/new-agent.agent.md` with YAML frontmatter
2. Define role, standards reference, workflow, and triggers
3. Document in this AGENTS.md file

### Adding a New Skill

1. Create `skills/skill-name/SKILL.md` with metadata
2. Document prerequisites, workflows, and examples
3. Reference from relevant agents

### Adding Instructions

1. Create `instructions/domain.instructions.md`
2. Set `applyTo` glob pattern in frontmatter
3. Update `instructions/INDEX.md`

## Agent Modularity

Agents are designed for **minimal context bloat** - each agent loads only what it needs:

**Modular Language Agents**:
- `bash.agent.md`, `python.agent.md`, `rust.agent.md` - Separate, focused agents
- Each references `skills/language-optimization/` for common patterns
- No context bloat: Load Bash agent without loading Python/Rust content
- Maintains DRY: Common patterns extracted to shared skill

**Modular MCP Agents**:
- `python-mcp-expert.agent.md`, `typescript-mcp-expert.agent.md` - Separate, focused agents
- Each references `skills/mcp-development/` for common MCP patterns
- No context bloat: Load Python MCP agent without loading TypeScript content
- Maintains DRY: Common MCP principles extracted to shared skill

**AI Configuration** (Clear Separation):
- `copilot-tuner.agent.md` - Handles Copilot instructions, CLAUDE.md, MCP configs
- `agents-maintainer.agent.md` - Exclusively handles AGENTS.md files
- No overlap or conflict

**Shared Skills**:
- `agent-patterns/` - Reusable workflow templates, model selection guidelines, tool profiles
- `language-optimization/` - Common optimization patterns across Bash, Python, Rust
- `mcp-development/` - Common MCP server development patterns

**Benefits**:
- **No context bloat**: Load only the agent you need
- **DRY maintained**: Common patterns in skills, not duplicated in agents
- **Modular**: Each agent is lean and focused
- **Scalable**: Easy to add new language agents referencing existing skills

---

*Last Updated: February 2026*
*Repository: Ven0m0/.github*
