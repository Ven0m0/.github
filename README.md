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

Scoped by file type in `.github/instructions/`:

| File | Applies To |
|------|------------|
| `actions.instructions.md` | `.github/workflows/*.yml` |
| `bash.instructions.md` | `*.sh`, `*.bash` |
| `javascript.instructions.md` | `*.js`, `*.ts`, `*.jsx`, `*.tsx` |
| `python.instructions.md` | `*.py` |
| `rust.instructions.md` | `*.rs` |
| `markdown.instructions.md` | `*.md` |

## Reusable Workflows

Call from any repository:

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
```

Available: `comprehensive-lint.yml`, `bun.yml`, `uv-lock.yml`, `dependabot-automerge.yml`, `img-opt.yml`, `git-maintenance.yml`, `release.yml`, `security.yml`, `docker-build.yml`, `rust.yml`, `go.yml`

## Overriding

Local files in a repository take precedence over these defaults.
