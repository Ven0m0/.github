---
description: 'Guidelines for creating prompt files for GitHub Copilot'
applyTo: '**/*.prompt.md'
---

# Copilot Prompt Files Guidelines

<HighLevelDetails>

- Naming: kebab-case, `.prompt.md` extension, stored in `.github/prompts/`
- Docs: https://code.visualstudio.com/docs/copilot/customization/prompt-files

</HighLevelDetails>

## Frontmatter

```yaml
---
description: "Actionable outcome in one sentence"
mode: agent  # ask | edit | agent
tools: ['read', 'edit', 'search']
model: 'Claude Sonnet 4.6'  # Optional: inherit active model if omitted
---
```

- `description` (required): Single sentence, actionable outcome
- `mode` (required): `ask`, `edit`, or `agent`
- `tools` (recommended): Minimal set needed. List in preferred execution order
- `model` (optional): Declare when prompt depends on specific capability tier

<Standards>

**Structure**: `#` heading matching intent -> Mission/Directive -> Scope/Preconditions -> Inputs -> Workflow (steps) -> Output Expectations -> Quality Assurance

**Inputs**: `${input:variableName[:placeholder]}` for required values. Document fallback when missing.

**Style**: Direct imperative sentences ("Analyze", "Generate", "Summarize"). Short, unambiguous. No idioms or humor.

**Output**: Specify format, structure, location. Include success/failure criteria. Provide validation steps.

</Standards>

<WhatToAdd>

- Good/Bad examples or scaffolds the prompt should produce
- Reference tables (capabilities, status codes) inline
- Links to authoritative docs instead of duplicating guidance
- Validation steps (commands, diff checks, review prompts)

</WhatToAdd>

<Limitations>

- No destructive operations without guard rails
- No excessive tool permissions
- No vague workflow steps
- No missing input documentation

</Limitations>
