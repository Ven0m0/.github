# GitHub Base Configuration

This repository provides default community health files, reusable workflows, base configs, and AI instructions for all repositories under the Ven0m0 account. GitHub uses these files when a repository does not define its own versions.

## Repository Structure

```
.github/
├── .github/
│   ├── workflows/           # Reusable GitHub Actions workflows
│   │   ├── comprehensive-lint.yml
│   │   ├── bun.yml
│   │   ├── uv-lock.yml
│   │   ├── dependabot-automerge.yml
│   │   ├── img-opt.yml
│   │   ├── git-maintenance.yml
│   │   ├── release.yml
│   │   ├── security.yml
│   │   ├── docker-build.yml
│   │   ├── rust.yml
│   │   └── go.yml
│   ├── instructions/        # Copilot scoped instructions
│   │   ├── actions.instructions.md
│   │   ├── bash.instructions.md
│   │   ├── javascript.instructions.md
│   │   ├── python.instructions.md
│   │   ├── rust.instructions.md
│   │   ├── markdown.instructions.md
│   │   └── token-efficient.instructions.md
│   ├── skills/              # AI skill modules
│   ├── ISSUE_TEMPLATE/      # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── copilot-instructions.md
│   ├── dependabot.yml
│   └── FUNDING.yml
├── agents/                  # AI agent configurations
├── configs/                 # Base configs for other repos
│   ├── rust/
│   ├── go/
│   ├── python/
│   ├── typescript/
│   └── docker/
├── .editorconfig
├── .shellcheckrc
├── .megalinter.yml
├── biome.json
└── [community health files]
```

## Default Community Files

These files apply to all repositories in the account:

| File | Purpose |
|------|---------|
| `CODE_OF_CONDUCT.md` | Contributor Covenant v2.1 |
| `CONTRIBUTING.md` | Contribution guidelines |
| `SECURITY.md` | Security policy and vulnerability reporting |
| `SUPPORT.md` | Support channels |
| `.github/FUNDING.yml` | Sponsorship configuration |
| `.github/ISSUE_TEMPLATE/*` | Bug reports, feature requests |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template |

## Reusable Workflows

Call these workflows from any repository using `workflow_call`.

### Available Workflows

| Workflow | Purpose |
|----------|---------|
| `comprehensive-lint.yml` | Multi-tool linting (ShellHarden, MegaLinter) |
| `bun.yml` | Bun.js setup, testing, linting |
| `uv-lock.yml` | Python UV lock file updates |
| `dependabot-automerge.yml` | Auto-merge Dependabot PRs |
| `img-opt.yml` | Image optimization (WebP, AVIF) |
| `git-maintenance.yml` | Repository optimization |
| `release.yml` | GitHub release creation |
| `security.yml` | Security scanning (Trivy, CodeQL, Gitleaks) |
| `docker-build.yml` | Docker build and push to GHCR |
| `rust.yml` | Rust CI (fmt, clippy, test, deny) |
| `go.yml` | Go CI (lint, test, coverage) |

### Usage Example

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
    with:
      working_directory: "."

  security:
    uses: Ven0m0/.github/.github/workflows/security.yml@main
    with:
      scan_dependencies: true
      scan_secrets: true
      scan_sast: true

  docker:
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    with:
      push: ${{ github.event_name != 'pull_request' }}

  release:
    needs: [lint, security]
    if: github.ref == 'refs/heads/main'
    uses: Ven0m0/.github/.github/workflows/release.yml@main
```

## Base Configs

Copy these configurations to your projects for consistent tooling.

### Rust

```bash
# Copy to project root
cp configs/rust/rustfmt.toml .
cp configs/rust/clippy.toml .
cp configs/rust/deny.toml .
# Use template for new projects
cp configs/rust/Cargo.toml.template Cargo.toml
```

### Go

```bash
cp configs/go/.golangci.yml .
cp configs/go/goreleaser.yaml .goreleaser.yaml
```

### Python

```bash
# For pyproject.toml projects
cp configs/python/pyproject.toml.template pyproject.toml
# Or standalone ruff
cp configs/python/ruff.toml .
```

### TypeScript/Node

```bash
cp configs/typescript/tsconfig.base.json .
cp configs/typescript/vitest.config.ts .
# Use template for new projects
cp configs/typescript/package.json.template package.json
```

### Docker

```bash
# Choose appropriate Dockerfile
cp configs/docker/Dockerfile.node Dockerfile
cp configs/docker/.dockerignore .
cp configs/docker/docker-compose.yml.template docker-compose.yml
```

## Copilot Instructions

Organization-wide instructions in `.github/copilot-instructions.md` apply to all repositories.

Scoped instructions in `.github/instructions/*.instructions.md` apply to specific file patterns:

| File | Scope |
|------|-------|
| `actions.instructions.md` | `.github/workflows/*.yml` |
| `bash.instructions.md` | `*.sh`, `*.bash` |
| `javascript.instructions.md` | `*.js`, `*.ts`, `*.jsx`, `*.tsx` |
| `python.instructions.md` | `*.py` |
| `rust.instructions.md` | `*.rs` |
| `markdown.instructions.md` | `*.md` |

## Pre-commit

Copy `.pre-commit-config.yaml` to enable pre-commit hooks:

```bash
cp .pre-commit-config.yaml /path/to/your/repo/
cd /path/to/your/repo
pip install pre-commit
pre-commit install
```

## Linting Configuration

Root-level configs that apply organization-wide:

| File | Tool |
|------|------|
| `biome.json` | Biome (JS/TS/JSON/CSS) |
| `.shellcheckrc` | ShellCheck |
| `.megalinter.yml` | MegaLinter |
| `.editorconfig` | Universal editor settings |
| `yamlfmt.yml` | YAML formatting |
| `.prettierrc` | Prettier (Markdown/prose) |

## Overriding Defaults

If a repository includes its own copy of a file, GitHub prefers the local file. Keep overrides small and specific. To override:

1. Copy the file to your repository
2. Modify as needed
3. Commit to your repository

## Maintenance

Changes here affect all repositories in the account. Follow these guidelines:

1. Test reusable workflows in a sandbox repository first
2. Keep updates conservative
3. Document breaking changes
4. Use conventional commits
