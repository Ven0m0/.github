---
name: workflow-development
description: Create, debug, and optimize GitHub Actions workflows with security best practices. Use when asked to "create workflow", "fix workflow", "add CI", or needs help with GitHub Actions.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Workflow Development Skill

Create, debug, and optimize GitHub Actions workflows.

Standards: See `instructions/cicd-standards.instructions.md`

## Security (Non-Negotiable)

```yaml
# SHA-pinned actions (CORRECT)
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2

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
- uses: actions/cache@0c907a75c2c80ebcb7f088228285e798b750cf8f
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
