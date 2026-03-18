---
description: 'Mise (mise-en-place) dev environment setup - tool versions, tasks, env vars, CI/CD, Docker integration'
mode: agent
---

# Mise Environment Setup

Dev environment management via [mise](https://mise.jdx.dev/). Handles tool versions, tasks, env vars, CI/CD pipelines, and Docker integration.

## Reference

- `.github/instructions/mise.instructions.md`

## Core Rules

- **Always check existing `mise.toml`** before suggesting changes
- **Use `mise use`** to add tools - never hand-edit `[tools]` section
- **Never modify `mise.local.toml`** - user-specific overrides, gitignored
- **Use loose versions** in `mise.toml` (`node = "22"`), exact pins only in `mise.lock`
- **Validate with `mise doctor`** before debugging environment issues manually

## Common Tasks

| Task | Command |
|------|---------|
| Add tool version | `mise use <tool>@<version>` |
| Add global tool | `mise use -g <tool>@<version>` |
| Create task | Add `[tasks.<name>]` to `mise.toml` |
| Create file task | Script in `mise-tasks/` with `#MISE` metadata |
| Set env var | Add to `[env]` section |
| Setup CI (GitHub Actions) | `jdx/mise-action@v3` with `cache: true` |
| Docker integration | Base image with `MISE_DATA_DIR`, shims on PATH |
| Debug environment | `mise doctor`, `mise config ls`, `mise env` |

## Workflow

1. **Assess**: Read `mise.toml`, check `mise config ls` for hierarchy
2. **Plan**: Present changes before modifying configs
3. **Apply**: Use `mise use` for tools, edit TOML for tasks/env/hooks
4. **Verify**: Run `mise doctor`, `mise install`, `mise ls --missing`
