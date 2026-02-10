---
name: codebase-cleanup
description: Use when preparing codebase for production, removing dead code, cleaning debug artifacts, or performing pre-merge cleanup passes.
---

# Codebase Cleanup

Remove clutter while preserving all functional behavior. **Cleanup only** - no refactoring or redesign.

## When to Use

- Preparing code for production commit
- Pre-merge cleanup passes
- Removing accumulated debug artifacts
- Dead code audits

## Core Principle

Be conservative. If unsure whether code is used, **flag it** instead of deleting.

## Quick Reference

| Category | Remove | Flag for Review |
|----------|--------|-----------------|
| Dead code | No references, commented-out blocks, unreachable | Reflection/dynamic calls, test-only refs |
| Debug | `print()`, `console.log()`, `debugger`, hardcoded test values | - |
| Imports | Unused | - |
| Comments | Restates obvious, outdated, inline changelogs | - |
| Temp names | `temp`, `test`, `debug`, `foo`, `xxx` | - |

## Execution Order

1. Identify removal candidates
2. Apply changes file-by-file
3. Update documentation (docstrings)
4. Run linters and formatters
5. Verify: check references, run tests

## Security Check

**Verify absence of**: Hardcoded credentials, API keys, internal URLs/IPs, PII in fixtures

**Confirm presence of**: Environment variable usage for secrets, proper `.gitignore` entries

## Linting Pass

```bash
# Python
ruff check --fix . && ruff format .

# JavaScript/TypeScript
eslint --fix . && prettier --write .
```

## Output

After cleanup, report:
- Files reviewed and modified
- Approximate lines removed
- Flagged items (file, line, concern)
- Recommended follow-ups outside cleanup scope

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Deleting code called via reflection | Flag instead; search for string references |
| Removing "unused" test utilities | Check test files first |
| Over-cleaning comments | Keep "why" explanations and warnings |
| Refactoring while cleaning | Separate concerns - cleanup only |
