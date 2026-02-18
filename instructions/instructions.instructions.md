---
description: 'Guidelines for creating custom instruction files for GitHub Copilot'
applyTo: '**/*.instructions.md'
---

# Custom Instructions File Guidelines

<HighLevelDetails>

- Format: Markdown with YAML frontmatter
- Naming: lowercase with hyphens (e.g., `react-best-practices.instructions.md`)
- Location: `.github/instructions/` or `instructions/` directory
- Docs: https://code.visualstudio.com/docs/copilot/customization/custom-instructions

</HighLevelDetails>

## Required Frontmatter

```yaml
---
description: "Brief description of purpose and scope"
applyTo: "**/*.ts,**/*.tsx"
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `description` | Yes | 1-500 chars, clearly states purpose |
| `applyTo` | Yes | Glob pattern(s) for target files |

Multiple patterns: `'**/*.ts,**/*.tsx,**/*.js'`. All files: `'**'`.

## Recommended Structure

1. **Title + Overview**: `#` heading, brief purpose and scope
2. **Core Sections**: General instructions, best practices, code standards, architecture, common patterns
3. **Examples**: GOOD/BAD code pairs with clear labels
4. **Validation** (optional): Build, lint, test commands

<Standards>

**Writing Style**: Imperative mood ("Use", "Implement", "Avoid"). Specific and actionable. No ambiguous terms ("should", "might").

**Content**:
- Concrete examples over abstract concepts
- Tables for comparing options and listing rules
- Current versions and best practices
- Links to official documentation

**XML Tags**: Use `<Goals>`, `<Standards>`, `<Limitations>`, `<Security>`, `<WhatToAdd>`, `<HighLevelDetails>` to structure content semantically for Copilot.

</Standards>

<Limitations>

- No overly verbose explanations
- No outdated information
- No ambiguous guidelines
- No missing code examples
- No contradictory advice
- No copy-paste from external docs (distill and contextualize)

</Limitations>
