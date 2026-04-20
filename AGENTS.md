# Ven0m0 `.github` Agent Guide

Repository defaults for community health files, reusable workflows and actions, agents, skills, and organization-wide AI guidance.

## Canonical files

| File | Role |
| --- | --- |
| `/home/runner/work/.github/.github/AGENTS.md` | Canonical repo guide for Claude Code and other agents |
| `/home/runner/work/.github/.github/CLAUDE.md` | Symlink to `AGENTS.md`; keep it that way |
| `/home/runner/work/.github/.github/copilot-instructions.md` | Canonical Copilot guidance |
| `/home/runner/work/.github/.github/.github/copilot-instructions.md` | Symlink to `../copilot-instructions.md` |

## What this repository ships

- Default community health files for Ven0m0 repositories
- Reusable GitHub Actions workflows in `/home/runner/work/.github/.github/.github/workflows`
- Custom reusable actions in `/home/runner/work/.github/.github/actions`
- Agent definitions in `/home/runner/work/.github/.github/agents`
- Skill modules in `/home/runner/work/.github/.github/skills`
- Scoped instruction files in `/home/runner/work/.github/.github/instructions`

## Repository map

| Path | Purpose |
| --- | --- |
| `/home/runner/work/.github/.github/.github` | GitHub default files, workflow templates, issue and PR templates |
| `/home/runner/work/.github/.github/agents` | Custom GitHub Copilot agents |
| `/home/runner/work/.github/.github/skills` | Reusable skill modules |
| `/home/runner/work/.github/.github/instructions` | File-pattern scoped guidance |
| `/home/runner/work/.github/.github/actions` | Composite and JavaScript actions |
| `/home/runner/work/.github/.github/.githooks` | Tracked Git hooks |
| `/home/runner/work/.github/.github/.vscode` | Editor and MCP configuration |
| `/home/runner/work/.github/.github/README.md` | Consumer-facing overview |
| `/home/runner/work/.github/.github/mise.toml` | Toolchain and task definitions |

## Guidance hierarchy

Use the smallest layer that can hold the rule.

1. `copilot-instructions.md` for short, always-loaded behavior
2. `AGENTS.md` for repo-level operating context
3. `instructions/*.instructions.md` for file-type or domain rules
4. `skills/*/SKILL.md` for task-specific workflows
5. Agent files in `agents/*.agent.md` for specialized execution roles

## Preferred skills

Load the matching skill before making non-trivial changes.

| Task | Skill |
| --- | --- |
| MCP-first search, reading, editing | `/home/runner/work/.github/.github/.github/skills/mcp-use/SKILL.md` |
| AI guidance tuning and deduplication | `/home/runner/work/.github/.github/.github/skills/ai-tuning/SKILL.md` |
| AI config linting | `/home/runner/work/.github/.github/.github/skills/linting-llm-configs/SKILL.md` |
| Workflow authoring and debugging | `/home/runner/work/.github/.github/.github/skills/workflow-development/SKILL.md` |
| Code cleanup | `/home/runner/work/.github/.github/.github/skills/code-maintenance/SKILL.md` |
| Readability and focused refactors | `/home/runner/work/.github/.github/.github/skills/clean-code/SKILL.md` |
| Bash, Python, and Rust optimization | `/home/runner/work/.github/.github/.github/skills/language-optimization/SKILL.md` |

## Development commands

Prefer the task runner in `/home/runner/work/.github/.github/mise.toml`.

| Task | Command |
| --- | --- |
| Install toolchain | `mise install` |
| Lint | `mise run lint` |
| Test | `mise run test` |
| Full check | `mise run check` |
| Format | `mise run format` |

### Direct validation commands

Use these when editing AI guidance or when you need focused checks.

| Scope | Command |
| --- | --- |
| AI context files | `npx -y @yawlabs/ctxlint --depth 3 --mcp --strict --fix --yes` |
| AI config linting | `npx -y agnix --fix-safe .` |
| Markdown, YAML, JSON formatting | `npx -y prettier --check .` |
| YAML lint | `uvx --from yamllint yamllint .` |
| Workflow lint | `actionlint` |
| Hook lint | `shellcheck .githooks/pre-commit` |
| Hook format check | `shfmt -d .githooks/pre-commit` |

## Change rules

- Use `rg` for discovery before editing.
- Prefer MCP tools over raw shell when an MCP tool can search, read, or edit more precisely.
- Keep root guidance concise; move deep procedures into `skills/` or `instructions/`.
- If a repo path is mentioned in guidance, it must exist in this repository.
- Update related docs when changing workflows, skills, agents, actions, or default templates.
- Preserve symlinks for `CLAUDE.md` and `.github/copilot-instructions.md`.
- Use conventional commits: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`.
- Keep branch names lowercase, descriptive, and hyphenated.

## Workflow authoring rules

When touching files in `/home/runner/work/.github/.github/.github/workflows`:

- Read `/home/runner/work/.github/.github/.github/skills/workflow-development/SKILL.md` first.
- Pin trusted actions to explicit major versions such as `actions/checkout@v6`.
- Add an explicit `permissions:` block.
- Set `timeout-minutes` on each job.
- Use path filters and concurrency when they reduce wasted runs.
- Prefer reusable workflows over duplicate inline job definitions.

## AI guidance authoring rules

When touching `AGENTS.md`, `CLAUDE.md`, `copilot-instructions.md`, skills, prompts, or instruction files:

- Keep the always-loaded files short and high-signal.
- Put stable repo facts here; put procedures and examples in skills.
- Remove duplicated rules instead of restating them in multiple files.
- Validate with `ctxlint` and `agnix` after edits.
- Do not invent directories, branches, commands, or workflow names.

## Critical secrets used by repository workflows

The workflow `/home/runner/work/.github/.github/.github/workflows/one-off-agent-prompt.yml` expects these repository secrets when the related providers are used:

- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY`
- `JULES_API_KEY`
- `OPENCODE_API_KEY`
- `OPENROUTER_API_KEY`
- `KILO_API_KEY`
- `KILO_ORG_ID`

Set them with GitHub secrets management, for example:

```bash
gh secret set ANTHROPIC_API_KEY
```

## Before opening a PR

- Run the smallest relevant validation set first, then `mise run check` when the change is broad.
- Review diffs for accidental generated churn.
- Confirm symlinks still resolve correctly.
- Update documentation that consumers rely on.

## References

- `/home/runner/work/.github/.github/README.md`
- `/home/runner/work/.github/.github/copilot-instructions.md`
- `/home/runner/work/.github/.github/instructions/INDEX.md`
- `/home/runner/work/.github/.github/.github/skills/ai-tuning/references/guide.md`
