# Ven0m0 `.github` Agent Guide

## Project Context

Default community health files, reusable workflows, actions, agents, skills, and organization-wide AI guidance for all Ven0m0 repositories. This repository is the source of truth for org-level Copilot instructions and agent definitions.

## Canonical files

| File                              | Role                                          |
| --------------------------------- | --------------------------------------------- |
| `AGENTS.md`                       | Canonical repo guide (this file)              |
| `CLAUDE.md`                       | Symlink to `AGENTS.md`; keep it that way      |
| `copilot-instructions.md`         | Canonical Copilot guidance                    |
| `.github/copilot-instructions.md` | Symlink to the root `copilot-instructions.md` |

## Repository map

| Path                       | Purpose                                                      |
| -------------------------- | ------------------------------------------------------------ |
| `.github/workflows/`       | Reusable CI/CD workflows                                     |
| `.github/instructions/`    | Copilot-scoped instruction files (subset of `instructions/`) |
| `.github/skills/`          | Copilot-scoped skill modules (subset of `skills/`)           |
| `actions/`                 | Composite and JavaScript actions                             |
| `agents/`                  | Custom GitHub Copilot agent definitions                      |
| `docs/`                    | HTML documentation and app manifests                         |
| `instructions/`            | File-pattern scoped guidance (index: `instructions/INDEX.md`)|
| `prompts/`                 | Reusable prompt templates                                    |
| `skills/`                  | Reusable skill modules                                       |
| `.githooks/`               | Tracked Git hooks                                            |
| `.vscode/`                 | Editor and MCP configuration                                 |
| `mise.toml`                | Toolchain and task definitions                               |

## Guidance hierarchy

Smallest layer wins. Place rules as low as possible.

1. `copilot-instructions.md` — always-loaded behavior (keep short)
2. `AGENTS.md` — repo operating context (this file)
3. `instructions/` — file-type and domain rules; see `instructions/INDEX.md`
4. `skills/` — task workflows and examples (one SKILL.md per directory)
5. `agents/` — specialized execution roles (each directory has an agent file)

## Skills — load first match

| Skill                  | When to load                                                |
| ---------------------- | ----------------------------------------------------------- |
| `mcp-use`              | Any MCP-first search, read, or edit                         |
| `ai-tuning`            | AGENTS.md, CLAUDE.md, Copilot, prompts, skills, instructions|
| `linting-llm-configs`  | Validating agent configs with `claudelint` or `agnix`       |
| `workflow-development` | `.github/workflows/` changes                                |
| `language-optimization`| Bash, Python, or Rust changes                               |
| `lint-and-validate`    | Repo-wide lint, format, or validation                       |
| `parallel-agents`      | Multi-agent or wave-based orchestration                     |
| `planning`             | Decomposing complex tasks into ordered plans                |
| `code-review`          | PR or diff review                                           |
| `docs-writer`          | Documentation generation or updates                         |

## Agents

| Agent                | Role                                                          |
| -------------------- | ------------------------------------------------------------- |
| `orchestrator`       | 5-phase pipeline driver (explore→plan→research→code→review)   |
| `planner`            | Task decomposition and wave-based execution plans             |
| `explorer`           | Codebase discovery and AST analysis                           |
| `researcher`         | External research and library evaluation                      |
| `coder`              | TDD-driven implementation specialist                          |
| `reviewer`           | Code review, security, and quality verification               |
| `debug`              | Bug investigation and root-cause analysis                     |
| `doc-writer`         | Documentation generation and updates                          |
| `git`                | Version control and branching operations                      |
| `janitor`            | Dead-code removal and codebase cleanup                        |
| `codebase-maintainer`| Post-implementation refactoring                               |
| `repo-architect`     | Agentic repo, MCP, and guidance tuning                        |
| `workflow-engineer`  | CI/CD pipeline design and maintenance                         |
| `frontend-specialist`| React, Next.js, and UI implementation                         |
| `arch-linux-expert`  | Platform-specific Arch Linux operations                       |

## Development commands

| Task              | Command           |
| ----------------- | ----------------- |
| Install toolchain | `mise install`    |
| Lint              | `mise run lint`   |
| Test              | `mise run test`   |
| Full check        | `mise run check`  |
| Format            | `mise run format` |

### Focused validation

| Scope              | Command                                                              |
| ------------------ | -------------------------------------------------------------------- |
| AI context files   | `npx -y @yawlabs/ctxlint --depth 5 --mcp --strict --fix --yes` (ctxlint) |
| Claude Code lint   | `npx -y claude-code-lint check-all --fix`                            |
| AI config linting  | `agnix --fix .`                                                      |
| Formatting check   | `npx -y prettier --check .`                                          |
| YAML lint          | `uvx --from yamllint yamllint .`                                     |
| Workflow lint      | `actionlint`                                                         |
| Hook lint          | `shellcheck .githooks/pre-commit`                                    |
| Hook format check  | `shfmt -d .githooks/pre-commit`                                      |

## Change rules

- Use `rg` for discovery before editing.
- Prefer MCP tools when they can search, read, or edit more precisely than raw shell.
- Keep root guidance concise; move procedures into `skills/` or `instructions/`.
- Verify every referenced path, command, workflow, skill, or agent with `rg`, `ctxlint`, or `agnix` before finishing.
- Update related docs when changing workflows, skills, agents, actions, or templates.
- Preserve the `CLAUDE.md` and `.github/copilot-instructions.md` symlinks.
- Conventional commit types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`.
- Branch names: lowercase, descriptive, hyphenated.

## Workflow rules

When editing `.github/workflows/`:

- Read `skills/workflow-development/SKILL.md` first.
- Use explicit action versions (e.g. `actions/checkout@v6`).
- Add a least-privilege `permissions:` block.
- Set `timeout-minutes` on each job.
- Prefer reusable workflows over duplicate inline jobs.

## AI guidance rules

When editing `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, skills, prompts, or instruction files:

- Keep always-loaded files short and high-signal.
- Put stable facts here; put procedures and examples in skills.
- Remove duplicated rules instead of restating them.
- Validate with `ctxlint`, `claude-code-lint`, and `agnix` after edits.
- Use only verified directories, commands, workflow names, and repo-specific examples.

## Workflow secrets

`.github/workflows/one-off-agent-prompt.yml` may require:

| Secret               | Purpose                    |
| -------------------- | -------------------------- |
| `ANTHROPIC_API_KEY`  | Claude / Anthropic models  |
| `GEMINI_API_KEY`     | Google Gemini models       |
| `JULES_API_KEY`      | Jules agent                |
| `OPENCODE_API_KEY`   | OpenCode agent             |
| `OPENROUTER_API_KEY` | OpenRouter model routing   |
| `KILO_API_KEY`       | Kilo Code agent            |
| `KILO_ORG_ID`        | Kilo Code organization ID  |

```bash
gh secret set ANTHROPIC_API_KEY
```
