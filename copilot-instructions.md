# GitHub Copilot Instructions

Repository defaults for the Ven0m0 `.github` repository.

## Load these skills first

- `mcp-use`
- `language-optimization`
- `ai-tuning` for AI guidance, prompts, skills, instructions, or agent files
- `linting-llm-configs` for agent-config validation
- `workflow-development` for `.github/workflows/` changes

## Repository facts

- This repository owns the default community health files for Ven0m0 repositories.
- Reusable workflows live in `.github/workflows/`.
- Custom agents live in `agents/`.
- Skills live in `skills/`.
- Scoped instructions live in `instructions/`.
- `CLAUDE.md` is a symlink to `AGENTS.md`.
- `.github/copilot-instructions.md` is a symlink to the root `copilot-instructions.md`.

## Source of truth

| Rule type                      | Canonical location        |
| ------------------------------ | ------------------------- |
| Short always-loaded behavior   | `copilot-instructions.md` |
| Repo operating context         | `AGENTS.md`               |
| File-type and domain standards | Files in `instructions/`  |
| Task workflows and examples    | Files in `skills/`        |

## Core commands

Prefer the task runner declared in `mise.toml`.

| Task              | Command           |
| ----------------- | ----------------- |
| Install toolchain | `mise install`    |
| Lint              | `mise run lint`   |
| Test              | `mise run test`   |
| Check             | `mise run check`  |
| Format            | `mise run format` |

## Required validation for AI guidance changes

Use `ctxlint` for context-file quality and `agnix` for agent-config linting after editing `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, `skills/*/SKILL.md`, `prompts/*.prompt.md`, or `instructions/*.instructions.md`.

| Task              | Command                                        |
| ----------------- | ---------------------------------------------- |
| Context lint      | `ctxlint --depth 3 --mcp --strict --fix --yes` |
| Agent config lint | `agnix --fix-safe .`                           |
| Formatting check  | `npx -y prettier --check .`                    |

## Editing rules

- Use `rg` for file discovery.
- Prefer MCP tools when an MCP tool can do the job more precisely.
- Keep changes small, specific, and repo-accurate.
- Verify every referenced path, command, workflow, skill, and agent with `rg`, `ctxlint`, or `agnix` before finishing the change.
- Keep this file concise; move deeper guidance into `AGENTS.md`, `skills/`, or `instructions/`.
- Update nearby documentation when changing reusable workflows, actions, skills, or agents.
- Preserve the `CLAUDE.md` and `.github/copilot-instructions.md` symlinks.

## Workflow rules

For files in `.github/workflows/`:

- Read `.github/skills/workflow-development/SKILL.md` first.
- Use explicit action versions.
- Add least-privilege `permissions:`.
- Set `timeout-minutes` on each job.
- Prefer reusable workflows over repeated inline jobs.

## Quality rules

- Use conventional commit types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`.
- Prefer readable, self-documenting names.
- Fail fast with specific error messages.
- Never hardcode secrets.
- Use repo-specific examples only after verifying they exist.

## Review checklist

- Correct file owns the rule
- Paths and commands exist
- Symlinks still resolve
- Required validation commands have been run
- Related documentation stays in sync
