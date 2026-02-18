---
name: workflow-development
description: Create, debug, and optimize GitHub Actions workflows with security best practices. Use when asked to "create workflow", "fix workflow", "add CI", or needs help with GitHub Actions.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
user-invocable: true
disable-model-invocation: false
---

# Workflow Development Skill

Create, debug, and optimize GitHub Actions workflows.

Standards: See `instructions/cicd-standards.instructions.md`

## Security (Non-Negotiable)

```yaml
# Example: Use version tags (see instructions/cicd-standards.instructions.md for org guidance)
- uses: actions/checkout@v4

# Minimal permissions
permissions:
  contents: read
```

## Reusable Workflow Pattern

```yaml
# Caller
jobs:
  ci:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: '3.12'
    secrets: inherit

# Definition
on:
  workflow_call:
    inputs:
      python-version:
        type: string
        default: '3.12'
```

## Debugging

| Error | Fix |
|-------|-----|
| Resource not accessible | Add to `permissions:` |
| Cache never hits | Check `hashFiles()` path |
| Secrets unavailable | `secrets: inherit` or explicit |
| Not triggered | Check `on:` config |

## Performance

```yaml
# Caching
- uses: actions/cache@v4
  with:
    path: ~/.cache/uv
    key: ${{ runner.os }}-uv-${{ hashFiles('uv.lock') }}

# Concurrency
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

# Matrix
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest]
```
