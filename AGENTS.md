# Ven0m0 .github Repository Guide

Organization-wide default community health files, Copilot instructions, AI agents, and development standards for all Ven0m0 repositories.

## Repository Overview

This repository provides:

- **Community Health Files**: Automatically used by GitHub when repositories don't define their own
- **Copilot Instructions**: Organization-wide and language-specific AI assistant guidance
- **AI Agents**: Specialized autonomous agents for development tasks
- **Skills**: Reusable knowledge modules for specific tools and workflows
- **Reusable Workflows**: GitHub Actions workflows for common CI/CD patterns
- **Development Standards**: Comprehensive code and workflow conventions

## Directory Structure

```
.github/
 agents/              # 21 specialized AI agents
 skills/              # 6 reusable skill modules
 instructions/        # 21 Copilot instruction files
 hooks/               # Pre-commit and custom hooks
 prompts/             # Reusable prompt templates
 .gemini/             # Google Gemini-specific configuration
‚    styleguide.md    # Gemini coding style guide
‚    commands/        # Gemini commands
‚    skills/          # Gemini-specific skills
 .github/workflows/   # Reusable GitHub Actions workflows
 AGENTS.md            # This file - comprehensive guide
 CLAUDE.md            # Claude AI instructions (symlinked to AGENTS.md)
 copilot-instructions.md  # Organization-wide Copilot guidance
 CODE_OF_CONDUCT.md   # Community standards
 CONTRIBUTING.md      # Contribution guidelines
 SECURITY.md          # Security policy
 SUPPORT.md           # Support channels
 README.md            # Quick reference
```

## Agents Ecosystem

The `@agents/` directory contains 21 specialized autonomous agents for common development tasks:

### Planning & Architecture
- **@agents/plan.agent.md** - Strategic planning and architecture assistant (opus)
- **@agents/implementation-plan.agent.md** - Detailed implementation strategy
- **@agents/prd.agent.md** - Product Requirements Document generator

### Code Optimization & Refactoring
- **@agents/bash.agent.md** - Bash/Shell optimization (shellcheck, shellharden, shfmt)
- **@agents/python.agent.md** - Python code optimization and modernization
- **@agents/rust.agent.md** - Rust performance and safety improvements
- **@agents/refactoring-expert.agent.md** - Code refactoring strategies
- **@agents/tdd-refactor.agent.md** - Test-driven refactoring workflows

### Development & Engineering
- **@agents/workflow-engineer.agent.md** - GitHub Actions and workflow expert
- **@agents/github-actions-expert.agent.md** - Advanced Actions configuration
- **@agents/github-issue-fixer.agent.md** - Issue triage and resolution
- **@agents/implementation-plan.agent.md** - Implementation strategy
- **@agents/task-planner.agent.md** - Task breakdown and planning
- **@agents/task-researcher.agent.md** - Research and discovery agent

### Repository & Knowledge Management
- **@agents/agents-maintainer.agent.md** - Agent ecosystem maintenance
- **@agents/repo-index.agent.md** - Repository indexing and search
- **@agents/profile-maintainer.agent.md** - Profile and metadata management
- **@agents/janitor.agent.md** - Repository cleanup and maintenance

### Quality & Analysis
- **@agents/critical-thinking.agent.md** - Deep analysis and questioning
- **@agents/context7.agent.md** - Extended context processing (7k token chunks)
- **@agents/copilot-tuner.agent.md** - Copilot instruction optimization
- **@agents/prompt-opt.agent.md** - Prompt engineering and optimization

### Agent YAML Metadata

Each agent uses this structure:

```yaml
---
name: agent-name
description: Brief description
applyTo: "**/*.ext" # File patterns this applies to
mode: agent
model: claude-4-5-[sonnet|opus]-latest
category: [specialized|planning|infrastructure]
modelParameters:
  temperature: 0.3-0.7 # Lower = deterministic, Higher = creative
tools: [codebase, semanticSearch, LSP, read, write, edit, search, ...]
---
```

**Model Selection**:
- **Sonnet** (0.3-0.4 temp): Code optimization, bug fixes, safe refactoring
- **Opus** (0.6-0.7 temp): Planning, architecture, complex analysis

## Skills Ecosystem

The `@skills/` directory contains 6 reusable knowledge modules:

### Available Skills

- **@skills/gh-cli/SKILL.md** - GitHub CLI comprehensive reference (v2.85.0+)
- **@skills/agentic-eval/SKILL.md** - Evaluating and improving agent performance
- **@skills/prd/SKILL.md** - Product Requirements Document best practices
- **@skills/ai-tuning/SKILL.md** - Fine-tuning AI instructions and prompts
- **@skills/refactor/SKILL.md** - Refactoring strategies and patterns
- **@skills/workflow-development/SKILL.md** - GitHub Actions and CI/CD workflows

Skills are referenced in agent instructions via frontmatter:

```yaml
skillReferences:
  - "@skills/gh-cli/SKILL.md"
  - "@skills/workflow-development/SKILL.md"
```

## Copilot Instructions

Organized in `@instructions/` directory - scoped by file type and domain.

### Organization-Wide
- **copilot-instructions.md** - Base guidance: code quality, git practices, security

### Language/Tool Specific
- **bash.instructions.md** - Shell scripting standards (modern tools: rg>grep, fd>find)
- **javascript.instructions.md** - JS/TS/JSX/TSX standards
- **python.instructions.md** - Python PEP 8/257 standards
- **rust.instructions.md** - Rust safety and performance
- **markdown.instructions.md** - Documentation standards
- **actions.instructions.md** - GitHub Actions workflow best practices

### Domain Specific
- **agent-skills.instructions.md** - Developing new skills
- **agents.instructions.md** - Creating and maintaining agents
- **ai-tuning.instructions.md** - Prompt and instruction optimization
- **code-review-generic.instructions.md** - Review methodology
- **memory-bank.instructions.md** - Persistent context patterns
- **performance-optimization.instructions.md** - Profiling and optimization
- **token-efficient.instructions.md** - Minimizing token usage
- **update-docs-on-code-change.instructions.md** - Doc sync patterns

## Development Workflows

### Standard Git Workflow

```bash
# 1. Create feature branch from main
git checkout -b feature/description

# 2. Make focused changes, test locally
# 3. Commit with conventional commit format
git commit -m "feat: add new agent"

# 4. Push branch
git push -u origin feature/description

# 5. Open PR via GitHub web UI or CLI
gh pr create --title "Feature: ..." --body "..."

# 6. Address review feedback
git add .
git commit -m "fix: address feedback"
git push

# 7. Merge via GitHub (squash/rebase per project settings)
```

### Conventional Commits

Format: `<type>(<scope>): <subject>`

Examples:
- `feat(agents): add copilot-tuner agent`
- `fix(bash): improve shellcheck error handling`
- `docs(skills): update gh-cli reference`
- `chore(workflows): bump action versions`
- `refactor(instructions): consolidate standards`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Pre-Commit Hooks

Located in `@hooks/` - run automated checks before commits.

Common checks:
- YAML/JSON validation
- Shell script linting (shellcheck)
- Markdown linting (markdownlint)
- Secret scanning
- Large file detection

### Reusable Workflows

Call from any repository:

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
```

Available:
- `comprehensive-lint.yml` - Multi-language linting
- `bun.yml` - JavaScript/TypeScript with Bun
- `uv-lock.yml` - Python with uv
- `dependabot-automerge.yml` - Automated dependency updates
- `img-opt.yml` - Image optimization
- `git-maintenance.yml` - Repository maintenance
- `release.yml` - Versioning and releases
- `security.yml` - Security scanning
- `docker-build.yml` - Container builds
- `rust.yml` - Rust projects
- `go.yml` - Go projects

## Key Conventions

### Code Standards

#### KISS Principle
Simple over clever. Readability first. Self-documenting code.

#### YAGNI Principle
Don't build features before they're needed. Avoid premature abstractions.

#### DRY Principle
Extract repeated logic into reusable components. Avoid duplication.

#### Naming
- Descriptive over abbreviated: `getUserById` not `getUsr`
- Functions: small, single responsibility
- Variables: clear intent

#### Fail Fast
- Validate early with specific error messages
- No silent failures or generic errors

#### Security First
- No secrets in logs/commits
- Validate inputs at system boundaries
- Use environment variables for credentials

#### Imports
Order: stdlib † third-party † local (alphabetical within each group)

#### Comments
Explain the "why", not the "what". Code should be self-documenting.

#### Changes
Minimal and focused. Don't clean up unrelated code in a PR.

### Tool Preferences

Modern tools prioritized (fast, feature-rich) with legacy fallbacks:

| Task | Preferred | Fallback |
|------|----------|----------|
| Search | `rg` | `grep` |
| Find Files | `fd` | `find` |
| Data (JSON) | `jaq` | `jq` |
| Data (YAML/XML) | `yq` | - |
| File Ops | `eza` | `ls` |
| View Files | `bat` | `cat` |
| Stream Edit | `sd` | `sed` |
| Archive | `zstd` | `xz` |
| Download | `aria2c` | `curl` > `wget` |
| Dev (JS) | `bun` | `npm` |
| Dev (Python) | `uv` | `pip` |
| Lint (Python) | `ruff` | `black` |
| Clone (Git) | `gix clone` | `git clone` |
| Fuzzy Select | `fzf` | - |

### Bash Standards

#### Template Structure

```bash
#!/usr/bin/env bash
# shellcheck enable=all shell=bash source-path=SCRIPTDIR
set -euo pipefail; shopt -s nullglob globstar
IFS=$'\n\t' LC_ALL=C

has(){ command -v -- "$1" &>/dev/null; }
msg(){ printf '%s\n' "$@"; }
log(){ printf '%s\n' "$@" >&2; }
die(){ printf '%s\n' "$1" >&2; exit "${2:-1}"; }
```

#### Bash Rules

- **Tests**: Use `[[ ]]`, regex `=~`
- **Arrays**: Use `mapfile -t`, `declare -A` for associative
- **Strings**: Use `${v//p/r}` (substitute), `${v%%p*}` (trim) - no sed for simple edits
- **I/O**: Use `<<<"$v"` (here-string), `< <(cmd)` (process substitution)
- **Performance**: Minimize forks, batch operations, precompile patterns
- **Forbidden**: `eval`, backticks, ls parsing, unquoted expansion, `expr`, remote source
- **Normalize**: `(){` (not `() {`), `>/` (not `> /`), `&>/dev/null` (not `>/dev/null 2>&1`)
- **Lint**: Run shellcheck, shellharden, shfmt

#### Performance Helper

```bash
fcat(){ printf '%s\n' "$(<${1})"; }  # Fast file concatenation
```

### Python Standards

- **PEP 8/257** compliance with 4-space indent
- **Type annotations** on all functions (typed returns)
- **Dataclasses** with `slots=True` for performance
- **Performance**: O(1) dict/set lookups, precompile regex, use `sys.stdin.read()`
- **Security**: Specific exception types only, avoid subprocess in hot paths
- **Optimization**: Run with `python3 -OO` flag

Example:

```python
from dataclasses import dataclass

@dataclass(slots=True)
class User:
    id: int
    name: str

    def get_display_name(self) -> str:
        """Return formatted display name."""
        return f"{self.name} (ID: {self.id})"
```

### Documentation Requirements

1. **Public APIs**: Must have documentation
2. **READMEs**: Quick start, installation, usage examples
3. **Complex Logic**: Inline comments explaining "why"
4. **Architecture**: ADRs (Architecture Decision Records) when applicable
5. **Code Comments**: Focus on non-obvious decisions, not stating the obvious

### Security

- Never commit secrets or credentials
- Use environment variables for sensitive data
- Validate inputs at system boundaries (user input, external APIs)
- Validate file uploads, API responses
- Don't trust internal code to validate - only external inputs

### Communication Style

- **No emojis** in code/documentation unless explicitly requested
- **No em dashes** (-) - use hyphens or words instead
- **Clear and direct** - avoid ambiguous language
- **Review first** - analyze before proposing changes
- **Avoid "successfully"** - provide evidence instead

## Integration with Gemini

The `@.gemini/` directory contains Google Gemini-specific configuration:

- **styleguide.md** - Gemini coding style guide
- **skills/** - Gemini-optimized skill modules
- **commands/** - Gemini command definitions

Note: Primary documentation in AGENTS.md applies to all AI assistants. Gemini-specific variations are in `.gemini/` subdirectory.

## Integration with Claude

Claude is the primary AI assistant for this organization. Instructions specific to Claude API behavior can be found in `copilot-instructions.md`. Claude-specific optimizations include:

- Extended context handling (via @agents/context7.agent.md)
- Tool use optimization for @skills/
- Integration with GitHub API via gh CLI

## Extending This Repository

### Adding a New Agent

1. Create `@agents/new-agent.agent.md` with YAML frontmatter
2. Define role, standards reference, workflow, and triggers
3. Add to categories (planning, specialized, infrastructure)
4. Document in this AGENTS.md file
5. Reference skills if applicable

### Adding a New Skill

1. Create `@skills/skill-name/SKILL.md` with metadata
2. Document prerequisites, core concepts, and examples
3. Reference from relevant agents
4. Add to this AGENTS.md file under Skills Ecosystem

### Adding Copilot Instructions

1. Create `@instructions/domain.instructions.md`
2. Start with scope (file patterns or domain)
3. Include principles, patterns, and examples
4. Reference from agents that apply
5. Update README

## Key Files Reference

| File | Purpose |
|------|---------|
| @copilot-instructions.md | Organization-wide Copilot guidance |
| @CODE_OF_CONDUCT.md | Community standards and expectations |
| @CONTRIBUTING.md | How to contribute to this repository |
| @SECURITY.md | Security policy and vulnerability reporting |
| @SUPPORT.md | Support channels and resources |
| @README.md | Quick reference and overview |
| @.editorconfig | Editor formatting standards |
| @.pre-commit-config.yaml | Pre-commit hook definitions |
| @.gitattributes | Git attributes for diff/merge |
| @.gitignore | Files to exclude from version control |

## Getting Started

1. **For Copilot Users**: Start with @copilot-instructions.md
2. **For Agent Development**: Review @agents/ and relevant @skills/
3. **For Code Contributions**: Read @CONTRIBUTING.md and language-specific @instructions/
4. **For Workflow**: Check @.github/workflows/ for CI/CD patterns
5. **For Security**: Review @SECURITY.md for reporting vulnerabilities

## Maintenance

- Agents are maintained in the @agents/ directory
- Skills are reviewed quarterly for accuracy and updates
- Instructions are synced with latest tool versions
- Use @agents/agents-maintainer.agent.md for ecosystem updates
- Use @agents/repo-index.agent.md to keep indexing current

---

*Last Updated: February 2026*
*Repository: Ven0m0/.github*
*Branch: main*
