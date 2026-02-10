The following instructions apply when performing a code review.

## Prompt File Guide

**Apply to files ending in `.prompt.md`**

- [ ] Has markdown frontmatter with `mode` (`agent`, `ask`, or `edit`) and `description`
- [ ] `description` is not empty
- [ ] Filename is lowercase with hyphens
- [ ] Encourage `tools` and strongly encourage `model` and `name`

## Instruction File Guide

**Apply to files ending in `.instructions.md`**

- [ ] Has markdown frontmatter with `description` and `applyTo`
- [ ] `description` is not empty
- [ ] `applyTo` specifies target file patterns (e.g., `'**/*.js,**/*.ts'`)
- [ ] Filename is lowercase with hyphens
- [ ] Uses XML tags (`<Goals>`, `<Standards>`, `<Limitations>`, `<Security>`, `<WhatToAdd>`, `<HighLevelDetails>`) for semantic structure

## Agent File Guide

**Apply to files ending in `.agent.md`**

- [ ] Has markdown frontmatter with `description`
- [ ] `description` is not empty
- [ ] Filename is lowercase with hyphens
- [ ] Encourage `tools`, strongly encourage `model` and `name`

## Agent Skills Guide

**Apply to folders in `skills/` directory**

- [ ] Contains `SKILL.md` with frontmatter (`name`, `description`)
- [ ] `name` is lowercase with hyphens, matches folder name
- [ ] `description` is 10-1024 chars, single-quoted, states WHAT/WHEN/KEYWORDS
- [ ] Bundled assets referenced in SKILL.md, under 5MB each
