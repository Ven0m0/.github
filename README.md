# .github

Default community health files and Copilot instructions for all Ven0m0 repositories.

## What This Provides

GitHub automatically uses these files when a repository doesn't define its own:

| File | Purpose |
|------|---------|
| `CODE_OF_CONDUCT.md` | Contributor Covenant v2.1 |
| `CONTRIBUTING.md` | Contribution guidelines |
| `SECURITY.md` | Security policy |
| `SUPPORT.md` | Support channels |
| `.github/FUNDING.yml` | Sponsorship |
| `.github/ISSUE_TEMPLATE/*` | Issue templates |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template |

## Copilot Instructions

Organization-wide: `.github/copilot-instructions.md`

Scoped by file type in `instructions/`:

| File | Applies To |
|------|------------|
| `bash.instructions.md` | `*.sh`, `*.bash` |
| `python.instructions.md` | `*.py` |
| `javascript.instructions.md` | `*.js`, `*.ts`, `*.jsx`, `*.tsx` |
| `rust.instructions.md` | `*.rs` |
| `cicd-standards.instructions.md` | `.github/workflows/*.yml` |
| `markdown.instructions.md` | `*.md` |

See `instructions/INDEX.md` for the full list.

## AI Agents

17 specialized agents in `agents/` for planning, code optimization, CI/CD, and more. See `AGENTS.md` for details.

## Skills

13 reusable knowledge modules in skills/, including `gh-cli`, `refactor`, `prd`, `ai-tuning`, `workflow-development`, `codebase-cleanup`, `code-review`, and `vibe-coding`.

## Reusable Workflows

Call from any repository:

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
```

Available: `comprehensive-lint.yml`, `bun.yml`, `uv-lock.yml`, `dependabot-automerge.yml`, `img-opt.yml`, `git-maintenance.yml`, `release.yml`, `security.yml`

## Overriding

Local files in a repository take precedence over these defaults.
