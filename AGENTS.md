# Ven0m0 `.github` Agent Guide

Repository defaults for community health files, reusable workflows and actions, custom agents, skills, and organization-wide AI guidance.

## Canonical files

| File                              | Role                                          |
| --------------------------------- | --------------------------------------------- |
| `AGENTS.md`                       | Canonical repo guide                          |
| `CLAUDE.md`                       | Symlink to `AGENTS.md`; keep it that way      |
| `copilot-instructions.md`         | Canonical Copilot guidance                    |
| `.github/copilot-instructions.md` | Symlink to the root `copilot-instructions.md` |

## What this repository owns

- Default community health files and templates in `.github/`
- Reusable workflows in `.github/workflows/`
- Reusable actions in `actions/`
- Custom agent definitions in `agents/`
- Reusable skills in `skills/`
- Scoped instruction files in `instructions/`

## Repository map

| Path            | Purpose                                                 |
| --------------- | ------------------------------------------------------- |
| `.github/`      | Default GitHub files, templates, and reusable workflows |
| `agents/`       | Custom GitHub Copilot agents                            |
| `skills/`       | Reusable skill modules                                  |
| `instructions/` | File-pattern scoped guidance                            |
| `actions/`      | Composite and JavaScript actions                        |
| `.githooks/`    | Tracked Git hooks                                       |
| `.vscode/`      | Editor and MCP configuration                            |
| `README.md`     | Consumer-facing overview                                |
| `mise.toml`     | Toolchain and task definitions                          |

## Guidance hierarchy

Use the smallest layer that can hold the rule.

1. `copilot-instructions.md` for short, always-loaded behavior
2. `AGENTS.md` for repo operating context
3. `instructions/*.instructions.md` for file-type and domain rules
4. `skills/*/SKILL.md` for task workflows and examples
5. `agents/*.agent.md` for specialized execution roles

## Skills to load first

- `mcp-use` for MCP-first search, reading, and edits
- `language-optimization` for Bash, Python, and Rust changes
- `ai-tuning` for AGENTS, CLAUDE, Copilot, prompts, skills, and instructions
- `linting-llm-configs` when validating agent configuration files
- `workflow-development` for `.github/workflows/` changes

## Development commands

Prefer the task runner declared in `mise.toml`.

| Task              | Command           |
| ----------------- | ----------------- |
| Install toolchain | `mise install`    |
| Lint              | `mise run lint`   |
| Test              | `mise run test`   |
| Full check        | `mise run check`  |
| Format            | `mise run format` |

### Focused validation commands

| Scope             | Command                                        |
| ----------------- | ---------------------------------------------- |
| AI context files  | `ctxlint --depth 3 --mcp --strict --fix --yes` |
| AI config linting | `agnix --fix-safe .`                           |
| Formatting check  | `npx -y prettier --check .`                    |
| YAML lint         | `uvx --from yamllint yamllint .`               |
| Workflow lint     | `actionlint`                                   |
| Hook lint         | `shellcheck .githooks/pre-commit`              |
| Hook format check | `shfmt -d .githooks/pre-commit`                |

## Change rules

- Use `rg` for discovery before editing.
- Prefer MCP tools when they can search, read, or edit more precisely than raw shell.
- Keep root guidance concise; move deep procedures into `skills/` or `instructions/`.
- If guidance mentions a repo path, command, workflow, skill, or agent, verify it with `rg`, `ctxlint`, or `agnix` before you finish.
- Update related docs when changing workflows, skills, agents, actions, or templates.
- Preserve the `CLAUDE.md` and `.github/copilot-instructions.md` symlinks.
- Use conventional commit types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`.
- Keep branch names lowercase, descriptive, and hyphenated.

## Workflow rules

When editing `.github/workflows/`:

- Read `.github/skills/workflow-development/SKILL.md` first.
- Use explicit action versions such as `actions/checkout@v6`.
- Add an explicit `permissions:` block.
- Set `timeout-minutes` on each job.
- Prefer reusable workflows over duplicate inline jobs.

## AI guidance rules

When editing `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, skills, prompts, or instruction files:

- Keep always-loaded files short and high-signal.
- Put stable repo facts here; put procedures and examples in skills.
- Remove duplicated rules instead of restating them.
- Validate with `ctxlint` and `agnix` after edits.
- Use only verified directories, commands, workflow names, and repo-specific examples.

## Workflow secrets

`.github/workflows/one-off-agent-prompt.yml` may require these repository secrets:

- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY`
- `JULES_API_KEY`
- `OPENCODE_API_KEY`
- `OPENROUTER_API_KEY`
- `KILO_API_KEY`
- `KILO_ORG_ID`

Manage them with GitHub secrets tooling, for example:

```bash
gh secret set ANTHROPIC_API_KEY
```
