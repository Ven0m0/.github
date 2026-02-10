---
description: 'Guidelines for creating Agent Skills for GitHub Copilot'
applyTo: '**/.github/skills/**/SKILL.md,**/.claude/skills/**/SKILL.md'
---

# Agent Skills Guidelines

<HighLevelDetails>

Skills are self-contained folders with instructions and bundled resources that teach AI agents specialized capabilities. Unlike instructions (coding standards), skills enable task-specific workflows with scripts, examples, and templates.

- Portable across VS Code, Copilot CLI, and Copilot coding agent
- Progressive loading: only loaded when relevant to user's request
- Location: `.github/skills/<name>/` (project) or `~/.github/skills/<name>/` (personal)

</HighLevelDetails>

## Required SKILL.md Format

```yaml
---
name: webapp-testing
description: 'Toolkit for testing local web apps using Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture screenshots, or check visual regressions. Supports Chrome, Firefox, and WebKit.'
license: Complete terms in LICENSE.txt
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Lowercase, hyphens, max 64 chars |
| `description` | Yes | Max 1024 chars, must state WHAT/WHEN/KEYWORDS |
| `license` | No | Reference to LICENSE.txt or SPDX identifier |

<Goals>

The `description` is the PRIMARY mechanism for skill discovery. Copilot reads ONLY `name` and `description` to decide whether to load a skill.

Include:
1. **WHAT** the skill does (capabilities)
2. **WHEN** to use it (triggers, scenarios, file types)
3. **Keywords** users might mention in prompts

</Goals>

## Body Sections

| Section | Purpose |
|---------|---------|
| `# Title` | Brief overview |
| `## When to Use` | Scenarios (reinforces description) |
| `## Prerequisites` | Required tools, dependencies |
| `## Step-by-Step Workflows` | Numbered task steps |
| `## Troubleshooting` | Common issues table |
| `## References` | Links to bundled docs |

## Bundled Resources

| Folder | Purpose | Loaded |
|--------|---------|--------|
| `scripts/` | Executable automation | On execution |
| `references/` | Docs the agent reads | When referenced |
| `assets/` | Static files used AS-IS | Never into context |
| `templates/` | Starter code agent MODIFIES | When referenced |

**Rule**: Agent reads and builds on content = `templates/`. File used as-is in output = `assets/`.

## Progressive Loading

| Level | Loads | When |
|-------|-------|------|
| Discovery | `name` + `description` | Always (lightweight) |
| Instructions | Full SKILL.md body | When request matches |
| Resources | Scripts, docs, templates | When explicitly needed |

<Standards>

- Imperative mood: "Run", "Create", "Configure"
- Include exact commands with parameters
- Scripts: include `--help`, handle errors, no stored credentials
- Keep SKILL.md under 500 lines; split into `references/` for large content
- Relative paths for all resource references

</Standards>

<Limitations>

- `name` must match folder name
- `description` must be 10-1024 characters, single-quoted
- No hardcoded credentials in scripts
- Assets must be under 5MB per file
- Bundle scripts only when: same code would be rewritten repeatedly, deterministic reliability needed, or complex logic benefits from pre-testing

</Limitations>
