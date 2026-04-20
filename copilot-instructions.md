# GitHub Copilot Instructions

Organization-wide defaults for the Ven0m0 `.github` repository.

## Load these skills first

- `mcp-use`
- `language-optimization`
- `ai-tuning` when editing AI guidance, prompts, instructions, skills, or agent files
- `linting-llm-configs` when validating agent configuration files
- `workflow-development` when editing files in `.github/workflows`

## Repository facts

- This repository owns the default community health files for Ven0m0 repositories.
- Reusable workflows live in `/home/runner/work/.github/.github/.github/workflows`.
- Custom agents live in `/home/runner/work/.github/.github/agents`.
- Skills live in `/home/runner/work/.github/.github/skills`.
- Scoped instructions live in `/home/runner/work/.github/.github/instructions`.
- `CLAUDE.md` is a symlink to `/home/runner/work/.github/.github/AGENTS.md`.
- `.github/copilot-instructions.md` is a symlink to `/home/runner/work/.github/.github/copilot-instructions.md`.

## Source of truth

Use the smallest file that fits the rule.

| Rule type | Canonical location |
| --- | --- |
| Short always-loaded behavior | `/home/runner/work/.github/.github/copilot-instructions.md` |
| Repo operating context | `/home/runner/work/.github/.github/AGENTS.md` |
| File-type or domain standards | `/home/runner/work/.github/.github/instructions/*.instructions.md` |
| Task workflows and deep examples | `/home/runner/work/.github/.github/skills/*/SKILL.md` |

## Core commands

Prefer the task runner declared in `/home/runner/work/.github/.github/mise.toml`.

| Task | Command |
| --- | --- |
| Install toolchain | `mise install` |
| Lint | `mise run lint` |
| Test | `mise run test` |
| Check | `mise run check` |
| Format | `mise run format` |

## Required validation for AI guidance changes

Run these after editing `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, skills, prompts, or instruction files.

| Task | Command |
| --- | --- |
| Context lint | `npx -y @yawlabs/ctxlint --depth 3 --mcp --strict --fix --yes` |
| Agent config lint | `npx -y agnix --fix-safe .` |
| Formatting check | `npx -y prettier --check .` |

## Editing rules

- Use `rg` for file discovery.
- Prefer MCP tools over generic shell commands when an MCP tool can do the work.
- Keep changes small, specific, and repo-accurate.
- If you reference a repo path, command, workflow, skill, or agent, verify that it exists.
- Do not duplicate long guidance across `copilot-instructions.md`, `AGENTS.md`, and skill files.
- Move detailed procedures into `skills/` or `instructions/`; keep this file concise.
- Update nearby documentation when changing reusable workflows, actions, skills, or agents.
- Preserve the `CLAUDE.md` and `.github/copilot-instructions.md` symlinks.

## Workflow rules

For files in `/home/runner/work/.github/.github/.github/workflows`:

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
- Do not invent examples that look like real repo paths unless those paths exist.

## Review checklist

- Correct file owns the rule
- Paths and commands exist
- Symlinks still resolve
- Requested validation commands have been run
- Related documentation stays in sync
