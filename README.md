# GitHub base configuration

This repository provides default community health files, reusable workflows, and GitHub Copilot instructions for all repositories under the Ven0m0 account. GitHub uses these files when a repository does not define its own versions.

## Default community files
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- SECURITY.md
- SUPPORT.md
- .github/FUNDING.yml
- .github/ISSUE_TEMPLATE/*
- .github/PULL_REQUEST_TEMPLATE.md

## Copilot instructions
- .github/copilot-instructions.md applies to all repositories.
- .github/instructions/*.instructions.md adds file scoped guidance.

## Reusable workflows
Reusable workflows live in .github/workflows and are called with workflow_call. Example:

```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/comprehensive-lint.yml@main
```

## Overriding defaults
If a repository includes its own copy of a file, GitHub prefers the local file. Keep overrides small and specific.

## Maintenance
Changes here affect all repositories. Keep updates conservative, document behavior changes, and test reusable workflows in a sandbox repo when possible.
