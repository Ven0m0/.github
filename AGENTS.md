# Ven0m0 .github Repository Guide

> Use newer/faster/better tools when possible. Always search for the available mcp servers and tools before starting work. Use tools and skills whenever you can.

Organization-wide defaults: community health files, Copilot instructions, AI agents, reusable workflows, and development standards for all Ven0m0 repositories.

---

## Project Overview

**Ven0m0** delivers practical developer tools for automation, platform engineering, and AI-assisted development. This `.github` repository provides:

- **20 agents** (6 pipeline + 9 supporting + 5 standalone utilities) for planning, code optimization, CI/CD, documentation, debugging
- **24 reusable skill modules** (patterns, best practices, templates)
- **38 scoped instruction files** (language standards, CI/CD, quality, domain specialization)
- **Reusable GitHub Actions workflows** for multi-language CI
- **Copilot instruction files** (org-wide + file-type scoped)

---

## Repository Structure

```
.github/
  agents/            # 20 AI agents (pipeline + supporting + standalone utilities)
  skills/            # 24 reusable knowledge modules
  instructions/      # 37 language/domain standards
  hooks/             # Git pre-commit hooks
  prompts/           # Reusable prompt templates
  .gemini/           # Google Gemini commands and config
  .vscode/           # VS Code settings (MCP, extensions)
  .github/workflows/ # Reusable CI/CD workflows
  actions/           # Custom GitHub Actions (setup-bun, setup-node-pnpm, setup-uv)
  AGENTS.md          # This file
  CLAUDE.md          # Symlink → AGENTS.md
  GEMINI.md          # Symlink → AGENTS.md
  copilot-instructions.md       # Organization-wide Copilot instructions
  README.md          # Quick start for inherited repos
  CONTRIBUTING.md    # Contribution guidelines
  FUNDING.yml        # Sponsorship info
  dependabot.yml     # Dependency update automation
  .markdownlint.json # Markdown linting rules
  .megalinter.yml    # MegaLinter configuration
  .yamllint.yml      # YAML validation
  .editorconfig      # Editor settings (indent, line endings)
  actionlint.yaml    # GitHub Actions linting
  biome.json         # JavaScript/TypeScript formatting
  bunfig.toml        # Bun package manager config
  renovate.json      # Renovate dependency updates
  yamlfmt.yml        # YAML formatter config
  repo-command.yml   # Issue/PR automation rules
```

---

## AI Agents (20)

One unified pipeline. All orchestration, planning, and review innovations from prior Gemini and RUG pipelines have been merged into the single `orchestrator → explorer → planner → researcher → coder → reviewer` pipeline.

### Pipeline Agents

| Agent            | File                    | Model             | Purpose                                                           |
| ---------------- | ----------------------- | ----------------- | ----------------------------------------------------------------- |
| **Orchestrator** | `orchestrator.agent.md` | claude-sonnet-4-6 | Drives 5-phase pipeline; discuss, PRD, multi-plan, wave execution |
| **Explorer**     | `explorer.agent.md`     | claude-haiku-4-5  | Fast codebase scanning and mapping                                |
| **Planner**      | `planner.agent.md`      | claude-opus-4-6   | DAG-based task breakdown, wave assignments, pre-mortem, contracts |
| **Researcher**   | `researcher.agent.md`   | claude-opus-4-6   | Library investigation and best practices                          |
| **Coder**        | `coder.agent.md`        | claude-sonnet-4-6 | TDD-driven implementation                                         |
| **Reviewer**     | `reviewer.agent.md`     | claude-opus-4-6   | task/wave/plan scopes; OWASP; PRD compliance                      |

### Pipeline Workflow

```
[discuss + PRD] → explorer → planner → researcher → coder → reviewer
```

| Phase     | Artifact               | What It Produces                                       |
| --------- | ---------------------- | ------------------------------------------------------ |
| Explore   | `01-exploration.md`    | Codebase map, relevant files, patterns, risks          |
| Plan      | `02-plan.md`           | DAG tasks with wave assignments, contracts, pre-mortem |
| Research  | `03-research.md`       | Findings, best practices, library recommendations      |
| Implement | `04-implementation.md` | Changes made, files modified, tests added              |
| Review    | `05-review.md`         | Verdict (pass/fail/conditional), issues, suggestions   |

**Modes**: `auto` (uninterrupted) or `gated` (pause after each phase for approval)

**Invoke**: `@orchestrator [task description] --mode=auto|gated`

### Supporting Agents

Invokable by the orchestrator during any phase, or directly by the user.

| Agent                    | File                           | Purpose                                          |
| ------------------------ | ------------------------------ | ------------------------------------------------ |
| **Git Expert**           | `git.agent.md`                 | Version control, branching, GitHub CLI           |
| **Workflow Engineer**    | `workflow-engineer.agent.md`   | GitHub Actions, CI/CD                            |
| **GH AW Builder**        | `gh-aw-builder.agent.md`       | GitHub Agentic Workflows                         |
| **Frontend Specialist**  | `frontend-specialist.agent.md` | React/Next.js                                    |
| **Debug**                | `debug.agent.md`               | Bug finding and fixing                           |
| **Documentation Writer** | `doc-writer.agent.md`          | Technical docs (on request only)                 |
| **Codebase Maintainer**  | `codebase-maintainer.agent.md` | Cleanup, tech debt, PROJECT_INDEX                |
| **Arch Linux Expert**    | `arch-linux-expert.agent.md`   | Arch administration                              |
| **Repo Architect**       | `repo-architect.agent.md`      | Repository structure, AI config tuning, and ADRs |

### Standalone Utility Agents

Standalone agents for specific workflows — not part of the orchestrator pipeline.

| Agent                 | File                                      | Purpose                               |
| --------------------- | ----------------------------------------- | ------------------------------------- |
| **SWE**               | `swe-subagent.agent.md`                   | Senior engineer for direct tasks      |
| **QA**                | `qa-subagent.agent.md`                    | Test planning and bug hunting         |
| **Universal Janitor** | `janitor.agent.md`                        | Tech debt and dead code removal       |
| **GPT-5 Beast Mode**  | `gpt-5-beast-mode.agent.md`               | Autonomous GPT-5 task execution       |
| **One-Shot Planner**  | `one-shot-feature-issue-planner.agent.md` | Feature → GitHub issue (no follow-up) |

---

## Skills

Reusable knowledge modules in `skills/` directory. Select 1–3 relevant skills based on task domain.

### Architecture & Planning

- `planning/` — Requirements clarification, dynamic questioning, and PRD drafting
- `agent-patterns/` — Agent workflow patterns and templates
- `app-builder/` — Full-stack app scaffolding, rapid prototyping, and tech-stack detection
- `parallel-agents/` — Multi-agent coordination patterns

### Code Quality & Maintenance

- `code-maintenance/` — Refactoring, cleanup, tech debt removal
- `code-review/` — Structured review rubric for diffs/PRs
- `clean-code/` — Readability, maintainability, SOLID principles
- `language-optimization/` — Bash, Python, Rust optimization patterns
- `lint-and-validate/` — Linting, formatting, validation automation

### Frontend & UI

- `nodejs-best-practices/` — Node.js, Next.js, and NestJS architecture and patterns
- `docker-expert/` — Docker, containerization, Dockerfile best practices

### Specialization

- `mcp-development/` — Model Context Protocol server development and custom integrations
- `docs-writer/` — Documentation templates and standards (includes reusable doc structures)
- `gh-cli/` — GitHub CLI reference and workflows
- `ai-tuning/` — AI config optimization, validation, and token efficiency
- `fix-issue/` — Issue diagnosis and resolution patterns
- `pr-review/` — Pull request review templates and checklists
- `workflow-development/` — GitHub Actions workflow patterns
- `web-search/` — Consolidated web search and discovery patterns

---

## Instructions (38)

Scoped by language and domain in `instructions/`. Copilot automatically applies based on file type via `applyTo` patterns.

### Language Standards

| Language                  | File                         | Applies To                                |
| ------------------------- | ---------------------------- | ----------------------------------------- |
| **Bash/Shell**            | `bash.instructions.md`       | `*.sh`, `*.bash`                          |
| **Python**                | `python.instructions.md`     | `*.py`, `pyproject.toml`                  |
| **JavaScript/TypeScript** | `javascript.instructions.md` | `*.js`, `*.ts`, `*.jsx`, `*.tsx`, `*.mjs` |
| **Rust**                  | `rust.instructions.md`       | `*.rs`                                    |
| **Go**                    | `go.instructions.md`         | `*.go`                                    |
| **Java**                  | `java.instructions.md`       | `*.java`                                  |
| **Kotlin**                | `kotlin.instructions.md`     | `*.kt`, `*.kts`                           |
| **C++**                   | `cpp.instructions.md`        | `*.cpp`, `*.cc`, `*.cxx`, `*.h`           |
| **PowerShell**            | `powershell.instructions.md` | `*.ps1`, `*.psm1`                         |
| **cmd/Batch**             | `cmd.instructions.md`        | `*.bat`, `*.cmd`                          |
| **AutoHotkey**            | `autohotkey.instructions.md` | `*.ahk`                                   |

### Build & CI/CD

| Topic               | File                             | Applies To                             |
| ------------------- | -------------------------------- | -------------------------------------- |
| **Makefile**        | `makefile.instructions.md`       | `Makefile`, `*.mk`                     |
| **CI/CD Standards** | `cicd-standards.instructions.md` | YAML workflows, CI/CD, and deployment  |
| **Docker**          | `docker.instructions.md`         | `Dockerfile`, `docker-compose.yml`     |

### Code Quality & Standards

| Topic                 | File                                | Description                                       |
| --------------------- | ----------------------------------- | ------------------------------------------------- |
| **Quality Standards** | `quality-standards.instructions.md` | Code review, metrics, performance gates           |
| **Meta-Authoring**    | `meta-authoring.instructions.md`    | Agents, skills, instructions, prompts             |
| **AI Tuning**         | `ai-tuning.instructions.md`         | CLAUDE.md compression, token efficiency           |
| **Token Efficiency**  | `token-efficient.instructions.md`   | Context optimization                              |
| **Memory Bank**       | `memory-bank.instructions.md`       | Project context storage                           |
| **Agent Constraints** | `agent-constraints.instructions.md` | Shared constraints applied to all pipeline agents |

### Specialization & Domain

| Topic                   | File                                         | Purpose                               |
| ----------------------- | -------------------------------------------- | ------------------------------------- |
| **Frontend**            | `frontend.instructions.md`                   | UI/UX patterns, component design      |
| **Backend**             | `backend.instructions.md`                    | API design, database, services        |
| **Documentation**       | `documentation.instructions.md`              | Technical writing standards           |
| **Markdown**            | `markdown.instructions.md`                   | Markdown syntax and conventions       |
| **Code Review**         | `code-review.instructions.md`                | Review process and rubric             |
| **Context Engineering** | `context-engineering.instructions.md`        | Effective context management          |
| **Arch Linux**          | `arch-linux.instructions.md`                 | Arch Linux specific workflows         |
| **Flutter**             | `flutter.instructions.md`                    | Flutter/Dart development              |
| **Performance**         | `performance.instructions.md`                | Profiling, optimization, benchmarking |
| **HTML/CSS/Design**     | `html-css-style-color-guide.instructions.md` | Markup, styling, accessibility        |
| **MCP Development**     | `python-mcp-server.instructions.md`          | Building MCP servers in Python        |
| **Prompt Engineering**  | `prompt.instructions.md`                     | Effective prompt design               |
| **Update Docs**         | `update-docs-on-code-change.instructions.md` | Keep docs in sync with code           |
| **Taming Copilot**      | `taming-copilot.instructions.md`             | Copilot behavior tuning               |
| **UI/UX Pro**           | `ui-ux-pro-max.instructions.md`              | Advanced design patterns              |
| **File Reading**        | `file-reading-optimization.instructions.md`  | Efficient file analysis               |

---

## Development Workflows

### Git Workflow

1. **Create feature branch** from `main`:

   ```bash
   git checkout -b feature/description
   ```

2. **Make focused changes** with meaningful commits:

   ```bash
   git commit -m "feat(scope): description"
   ```

3. **Push and create PR**:

   ```bash
   git push -u origin feature/description
   gh pr create --title "Feature: ..." --body "..."
   ```

4. **Merge after approval**:
   ```bash
   git merge --squash feature/description  # or rebase-merge for history
   git push origin main
   ```

### Conventional Commits

Format: `<type>(<scope>): <subject>`

**Types**: `feat` (new), `fix` (bug), `docs` (docs), `style` (format), `refactor` (structure), `perf` (speed), `test` (tests), `chore` (maintenance)

**Examples**:

- `feat(agents): add debug agent`
- `fix(workflows): correct Python test coverage threshold`
- `docs(README): update quick-start example`
- `refactor(skills): consolidate code-maintenance patterns`

### Reusable Workflows

All repositories can call these workflows from `.github/`:

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main

  ci-typescript:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-bun.yml@main
    with:
      bun-version: "latest"
      coverage-threshold: 80

  ci-python:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: "3.12"
      coverage-threshold: 90
```

**Available reusable workflows**:

- `comprehensive-lint.yml` — Multi-language linting, shellharden, MegaLinter
- `reusable-ci-bun.yml` — Bun-based TypeScript/JavaScript CI (lint, typecheck, coverage, build, matrix)
- `reusable-ci-python.yml` — Python CI (uv, pytest, coverage)
- `reusable-release.yml` — Version/release automation
- `git-maintenance.yml` — Repository cleanup (branches, stale checks)
- `dependabot-automerge.yml` — Auto-merge dependency updates
- `security.yml` — SAST, CodeQL, dependency review
- `img-opt.yml` — Image optimization
- `uv-lock.yml` — Python lock file management

---

## Development Conventions

### Code Standards

**All Languages**:

- **KISS** — Simple over clever; readability first
- **YAGNI** — Don't build before needed
- **DRY** — Extract repeated logic
- **Fail Fast** — Validate early; specific error messages
- **Security** — No hardcoded secrets; validate at boundaries

**Test Coverage**: 80%+ minimum, 95%+ for critical paths

**Type Safety**: Full type annotations; no `any` without justification

**Error Handling**: Specific exceptions; no silent failures

### Tooling Preferences

| Task              | Preferred        | Fallback   | Windows       |
| ----------------- | ---------------- | ---------- | ------------- |
| Search            | `rg`             | `grep`     | `rg`          |
| Find files        | `fd`             | `find`     | `fd`          |
| JSON/YAML         | `jq`/`yq`        | -          | `jq`/`yq`     |
| Stream edit       | `sd`             | `sed`      | `sd`          |
| Download          | `aria2c`         | `curl`     | `aria2c`      |
| List              | `eza`            | `ls`       | `eza`         |
| View              | `bat`            | `cat`      | `bat`         |
| **JS/TS**         | `bun` (runner)   | `npm`      | `bun`         |
| **JS/TS Dev**     | `pnpm` (package) | `npm`      | `pnpm`        |
| **Python**        | `uv` (runner)    | `pip`      | `uv`          |
| **Lint (JS)**     | `biome`          | `eslint`   | `biome`       |
| **Format (JS)**   | `biome`          | `prettier` | `biome`       |
| **Lint (Python)** | `ruff`           | `black`    | `ruff`        |
| **Type (Python)** | `mypy --strict`  | -          | `mypy`        |
| **Test (Python)** | `pytest`         | `unittest` | `pytest`      |
| **Lint (Bash)**   | `shellcheck`     | -          | `shellcheck`  |
| **Format (Bash)** | `shfmt`          | -          | `shfmt`       |
| **Harden (Bash)** | `shellharden`    | -          | `shellharden` |

### Language-Specific

**Bash**: `set -euo pipefail`, quote variables, `[[ ]]` not `[ ]`, use `rg`/`fd` over `grep`/`find`

**Python**: PEP 8 + strict types, generators over lists, pathlib over os.path, f-strings, `uv` for package management

**JavaScript/TypeScript**: Strict mode, interfaces over type aliases, type guards instead of casts, stable array keys, semantic HTML, accessibility

**Rust**: idiomatic patterns, `cargo fmt`, `clippy` checks, owned by default

---

## Key Dependencies & Tooling

### CI/CD Infrastructure

- **GitHub Actions** — Workflows, reusable patterns, secrets, OIDC auth
- **MegaLinter** — Comprehensive multi-language linting
- **Dependabot** — Dependency updates with auto-merge
- **Renovate** — Alternative dep automation (configured in renovate.json)

### Language Runtimes

- **Node.js** (v20, v22) — TypeScript/JavaScript execution
- **Python** (3.12, 3.13) — Python execution and package management
- **Rust** (stable) — Compiled language support
- **Bun** — JavaScript runtime and bundler
- **Go, Java, Kotlin, C++** — Additional language support

### Linting & Formatting

- **biome** — JavaScript/TypeScript (formatter + linter, zero-config)
- **ruff** — Python (lint + format, extremely fast)
- **shellcheck** — Bash analysis
- **shfmt** — Bash formatting
- **shellharden** — Bash hardening
- **yamllint** — YAML validation
- **markdownlint** — Markdown validation
- **actionlint** — GitHub Actions linting

### Testing & Coverage

- **vitest** — JavaScript/TypeScript (Vite-native)
- **jest** — JavaScript/TypeScript (compatible)
- **pytest** — Python (comprehensive)
- **Codecov** — Coverage tracking
- **bun test** — Bun native testing

### Package Management

- **pnpm** — JavaScript/TypeScript (preferred, fast, strict)
- **bun** — JavaScript runtime + package manager
- **npm** — JavaScript fallback
- **uv** — Python (ultra-fast, replaces pip + venv)

### Type Checking

- **TypeScript** — `--strict` mode
- **mypy** — Python strict typing
- **biome** — JavaScript/TypeScript static analysis

---

## Common Development Tasks

### Feature Development

1. **Understand**: Read relevant instruction files, skill modules
2. **Plan**: Use Strategic Planner agent for architecture
3. **Implement**: Follow language standards; small commits
4. **Test**: 80%+ coverage minimum
5. **Review**: Code Review instructions; pass linters
6. **Merge**: Conventional commit; PR approval

**Commands**:

```bash
# TypeScript/JavaScript
bun install && bun run test --coverage && bun run build

# Python
uv sync && uv run pytest -v --cov && uv audit

# Bash
shellcheck script.sh && shfmt -i 2 -w script.sh && shellharden script.sh

# Comprehensive
bun run lint  # or: ruff check --fix && biome check --apply
```

### Bug Fixing

1. **Use Debug agent** for application bugs
2. **Use Language Optimizer** for code quality issues
3. **Root cause**: Critical Thinking agent for analysis
4. **Test-driven**: Write failing test first
5. **Verify**: All tests pass; no regressions

### Testing

- **Unit tests**: Logic isolation; fast feedback
- **Integration tests**: Component interaction
- **E2E tests**: Full workflows (where applicable)
- **Coverage**: 80%+ minimum; critical paths 95%+

### Dependency Management

- **Updates**: Dependabot (auto) or `renovate` (manual)
- **Audit**: `uv audit` (Python), `npm audit` (JS)
- **Lock files**: Commit `pnpm-lock.yaml`, `uv.lock` for reproducibility

### Documentation

1. **Update README** when adding features
2. **Maintain CHANGELOG** (if applicable)
3. **API docs**: Docstrings + generated docs
4. **Architecture**: Diagrams for complex systems
5. **Use Documentation Writer agent** on explicit request

---

## CI/CD Pipeline

### Pull Request (PR)

1. **Lint** — Comprehensive linting via MegaLinter
2. **Type Check** — TypeScript strict, Python mypy
3. **Test** — Unit + integration tests with coverage threshold
4. **Build** — Compile/transpile; verify artifacts
5. **Security** — CodeQL, dependency review, SAST
6. **Review** — Human or automated review

### Merge

1. **All checks pass** — No red status
2. **Coverage maintained** — No drops below threshold
3. **Approval** — At least 1 maintainer approval
4. **Squash/rebase-merge** — Clean history

### Deployment (Repo-Specific)

- Use `reusable-release.yml` for version bumping
- Tag releases with semantic versioning
- Build artifacts in CI (not locally)
- Secrets via GitHub Secrets or OIDC

---

## Overriding These Defaults

Local files in any repository take precedence:

- `copilot-instructions.md` — Repo-specific Copilot behavior
- `CLAUDE.md` — Repo-specific Claude Code behavior
- `AGENTS.md` — Repo-specific agent definitions
- Language instructions — Create repo's own `.github/instructions/`
- Workflows — Create repo's own `.github/workflows/`

Example: A repository with `python-only` focus can override Python version defaults:

```yaml
# .github/workflows/ci.yml in consuming repo
jobs:
  ci:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: "3.13" # Override default 3.12
      coverage-threshold: 95 # Stricter than org default 90
```

---

## Extending This Repository

### Adding a New Agent

1. Create `agents/new-agent.agent.md` with YAML frontmatter
2. Define role, reference standards, describe workflow
3. Document in this AGENTS.md file (add row to appropriate table)

### Adding a New Skill

1. Create `skills/skill-name/` directory
2. Create `skills/skill-name/SKILL.md` with metadata
3. Add prerequisites, workflows, examples
4. Update instructions/INDEX.md

### Adding Instructions

1. Create `instructions/domain.instructions.md`
2. Set `applyTo` glob pattern in YAML frontmatter
3. Add applicable standards and patterns
4. Update instructions/INDEX.md

### Reusable Workflows

1. Create `.github/workflows/reusable-xyz.yml`
2. Use `on: workflow_call:` trigger
3. Document in README.md
4. Version tag for stability

---

## MCP Integration

**Model Context Protocol** (MCP) servers available:

- **context7** — Up-to-date library documentation and examples
- **GitHub** — Repository, PR, issue operations (org-level)
- **Google Gemini** — Google cloud integration

Configure in agent YAML:

```yaml
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers:
      CONTEXT7_API_KEY: "${{ secrets.CONTEXT7_API_KEY }}"
```

---

## Quick Reference

| Task             | Command/Approach                                            |
| ---------------- | ----------------------------------------------------------- |
| Lint all         | `bun run lint` or `ruff check --fix && biome check --apply` |
| Test             | `bun test --coverage` or `uv run pytest -v --cov`           |
| Build            | `bun run build`                                             |
| Format           | `biome check --apply` (TS/JS) or `ruff format` (Python)     |
| Shell script     | `shellcheck`, `shfmt`, `shellharden`                        |
| Git setup        | `git checkout -b feature/name`                              |
| Commit           | `git commit -m "feat(scope): desc"`                         |
| PR create        | `gh pr create --title "Title" --body "Body"`                |
| Release          | Use `reusable-release.yml` workflow                         |
| Dependency audit | `uv audit` (Python) or `npm audit` (JS)                     |

---

## Resources

- **Instructions**: `instructions/` for language-specific standards
- **Skills**: `skills/` for domain knowledge modules
- **Agents**: `agents/` for specialized autonomous assistants
- **Workflows**: `.github/workflows/` for CI/CD patterns
- **Community**: See `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` in parent repos

---

**Last Updated**: March 2026
**Repository**: Ven0m0/.github
**Organization**: Ven0m0

# context-mode — MANDATORY routing rules

You have context-mode MCP tools available. These rules are NOT optional — they protect your context window from flooding. A single unrouted command can dump 56 KB into context and waste the entire session.

## BLOCKED commands — do NOT attempt these

### curl / wget — BLOCKED

Any Bash command containing `curl` or `wget` is intercepted and replaced with an error message. Do NOT retry.
Instead use:

- `ctx_fetch_and_index(url, source)` to fetch and index web pages
- `ctx_execute(language: "javascript", code: "const r = await fetch(...)")` to run HTTP calls in sandbox

### Inline HTTP — BLOCKED

Any Bash command containing `fetch('http`, `requests.get(`, `requests.post(`, `http.get(`, or `http.request(` is intercepted and replaced with an error message. Do NOT retry with Bash.
Instead use:

- `ctx_execute(language, code)` to run HTTP calls in sandbox — only stdout enters context

### WebFetch — BLOCKED

WebFetch calls are denied entirely. The URL is extracted and you are told to use `ctx_fetch_and_index` instead.
Instead use:

- `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` to query the indexed content

## REDIRECTED tools — use sandbox equivalents

### Bash (>20 lines output)

Bash is ONLY for: `git`, `mkdir`, `rm`, `mv`, `cd`, `ls`, `npm install`, `pip install`, and other short-output commands.
For everything else, use:

- `ctx_batch_execute(commands, queries)` — run multiple commands + search in ONE call
- `ctx_execute(language: "shell", code: "...")` — run in sandbox, only stdout enters context

### Read (for analysis)

If you are reading a file to **Edit** it → Read is correct (Edit needs content in context).
If you are reading to **analyze, explore, or summarize** → use `ctx_execute_file(path, language, code)` instead. Only your printed summary enters context. The raw file content stays in the sandbox.

### Grep (large results)

Grep results can flood context. Use `ctx_execute(language: "shell", code: "grep ...")` to run searches in sandbox. Only your printed summary enters context.

## Tool selection hierarchy

1. **GATHER**: `ctx_batch_execute(commands, queries)` — Primary tool. Runs all commands, auto-indexes output, returns search results. ONE call replaces 30+ individual calls.
2. **FOLLOW-UP**: `ctx_search(queries: ["q1", "q2", ...])` — Query indexed content. Pass ALL questions as array in ONE call.
3. **PROCESSING**: `ctx_execute(language, code)` | `ctx_execute_file(path, language, code)` — Sandbox execution. Only stdout enters context.
4. **WEB**: `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` — Fetch, chunk, index, query. Raw HTML never enters context.
5. **INDEX**: `ctx_index(content, source)` — Store content in FTS5 knowledge base for later search.

## Subagent routing

When spawning subagents (Agent/Task tool), the routing block is automatically injected into their prompt. Bash-type subagents are upgraded to general-purpose so they have access to MCP tools. You do NOT need to manually instruct subagents about context-mode.

## Output constraints

- Keep responses under 500 words.
- Write artifacts (code, configs, PRDs) to FILES — never return them as inline text. Return only: file path + 1-line description.
- When indexing content, use descriptive source labels so others can `ctx_search(source: "label")` later.

## ctx commands

| Command       | Action                                                                                |
| ------------- | ------------------------------------------------------------------------------------- |
| `ctx stats`   | Call the `ctx_stats` MCP tool and display the full output verbatim                    |
| `ctx doctor`  | Call the `ctx_doctor` MCP tool, run the returned shell command, display as checklist  |
| `ctx upgrade` | Call the `ctx_upgrade` MCP tool, run the returned shell command, display as checklist |
