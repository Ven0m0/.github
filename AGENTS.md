# Ven0m0 .github Repository Guide

Organization-wide default community health files, Copilot instructions, AI agents, and development standards for all Ven0m0 repositories.

## Directory Structure

```
.github/
  agents/            # 12 specialized AI agents
  skills/            # 10 reusable skill modules
  instructions/      # 17 Copilot instruction files
  hooks/             # Pre-commit hooks
  prompts/           # Reusable prompt templates
  .gemini/           # Google Gemini configuration
  .github/workflows/ # Reusable GitHub Actions workflows
  AGENTS.md          # This file
  CLAUDE.md          # Symlink to AGENTS.md
  copilot-instructions.md
```

## Agents

The `agents/` directory contains 12 specialized autonomous agents:

### Workflow Orchestration

| Agent | Purpose |
|-------|---------|
| `multi-agent-workflow.agent.md` | Multi-agent workflow: planning, execution, refactoring, cleanup, review |

### Planning & Architecture

| Agent | Purpose |
|-------|---------|
| `strategic-planner.agent.md` | PRDs to implementation plans (opus) |
| `task-researcher.agent.md` | Deep research for task planning |

### Code Optimization

| Agent | Purpose |
|-------|---------|
| `language-optimizer.agent.md` | Bash, Python, Rust optimization and refactoring (language-branching) |

### Development & Engineering

| Agent | Purpose |
|-------|---------|
| `git.agent.md` | Git & GitHub CLI workflows |
| `workflow-engineer.agent.md` | GitHub Actions and CI/CD |
| `github-issue-fixer.agent.md` | Issue triage and resolution |

### Repository & Knowledge Management

| Agent | Purpose |
|-------|---------|
| `codebase-maintainer.agent.md` | Cleanup and indexing (janitor + repo-index consolidated) |
| `profile-maintainer.agent.md` | GitHub profile README management |

### Quality & Analysis

| Agent | Purpose |
|-------|---------|
| `critical-thinking.agent.md` | Deep analysis and questioning |
| `context7.agent.md` | Documentation-powered assistant (Context7) |
| `ai-config-expert.agent.md` | AI config: Copilot, CLAUDE.md, AGENTS.md, prompts |
| `arch-linux-expert.agent.md` | Arch Linux specialist |

### Agent Metadata

```yaml
---
name: agent-name
description: Brief description
model: claude-4-6-[sonnet|opus|haiku]-latest
tools: [codebase, read, write, edit, search, ...]
---
```

- **Sonnet** (0.3-0.4 temp): Code optimization, bug fixes, safe refactoring
- **Opus** (0.6-0.7 temp): Planning, architecture, complex analysis

## Skills

The `skills/` directory contains 10 reusable knowledge modules:

| Skill | Purpose |
|-------|---------|
| `gh-cli/` | GitHub CLI reference |
| `prd/` | PRD best practices |
| `ai-tuning/` | AI config optimization + CLAUDE.md condensation |
| `code-maintenance/` | Refactoring and cleanup (refactor + codebase-cleanup consolidated) |
| `workflow-development/` | GitHub Actions workflows |
| `agent-patterns/` | Agent workflow patterns and templates |
| `language-optimization/` | Common optimization patterns (Bash, Python, Rust) |
| `mcp-development/` | MCP server development (Python, TypeScript) |
| `code-review/` | Structured review rubric for diffs/PRs |
| `vibe-coding/` | Fast local web app prototyping |

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
| `meta-authoring.instructions.md` | Agents, skills, instructions, prompts |
| `ai-tuning.instructions.md` | CLAUDE.md, copilot-instructions.md, output compression |

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

## Agent Consolidation

**Language Optimizer** (bash + python + rust + refactoring-expert):
- Single agent with language-branching; auto-detects from file type
- References `skills/language-optimization/`, `skills/code-maintenance/`

**Codebase Maintainer** (janitor + repo-index):
- Cleanup mode: remove dead code, simplify, dependency hygiene
- Index mode: PROJECT_INDEX.md, token-efficient context

**Skills consolidated**: refactor + codebase-cleanup → code-maintenance; condense → ai-tuning
**Instructions consolidated**: agents + agent-skills + instructions + prompt → meta-authoring; token-efficient → ai-tuning

**MCP Integration**: Repository agents compatible with GitHub.com; MCP at org/enterprise level

---

*Last Updated: February 2026*
*Repository: Ven0m0/.github*
