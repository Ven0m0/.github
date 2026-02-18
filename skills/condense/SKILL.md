---
name: condense
description: Deduplicate and consolidate CLAUDE.md memory files. Use when asked to "condense CLAUDE.md", "deduplicate memory files", or "consolidate instructions". Removes redundancy within files and across the hierarchy.
user-invocable: true
disable-model-invocation: true
---

# CLAUDE.md Condensation

Deduplicate and consolidate CLAUDE.md memory files to remove redundancy.

## Workflow

### Phase 1: Discovery

Find all CLAUDE.md files and analyze for:
1. Intra-file duplication (same instruction repeated within a file)
2. Cross-file duplication (same instruction in multiple files)
3. Misplaced instructions (subdirectory files containing project-wide content)

### Phase 2: Analysis

- **Intra-file**: Repeated bullets, semantically similar content
- **Cross-file**: Root CLAUDE.md = project-wide; subdirectory = directory-specific only
- **Misplaced**: Subdirectory instruction applies project-wide -> move to root

### Phase 3: Present Findings

For each issue: show duplicated content, affected files, proposed consolidation (delete, move, merge). Wait for user approval.

### Phase 4: Implement

1. **Remove duplicates** - keep in most appropriate location
2. **Move misplaced** - transfer to correct hierarchy level
3. **Merge similar** - combine semantically similar instructions

## Hierarchy Rules

- `./CLAUDE.md` - Project-wide instructions (highest priority)
- `./.claude/rules/*.md` - Topic-specific rules (modular)
- `./subdir/CLAUDE.md` - Only directory-specific instructions
- `~/.claude/CLAUDE.md` - Personal preferences across all projects
- `./CLAUDE.local.md` - Personal project-specific (not shared)
