---
name: code-maintenance
description: Refactoring and cleanup. Use when improving structure, removing dead code, eliminating duplication, or pre-merge cleanup.
user-invocable: true
disable-model-invocation: false
---

# Code Maintenance

Refactoring (structure) and cleanup (removal). Behavior preserved. Gradual evolution.

## When to Use

| Scenario | Focus |
|----------|-------|
| Code hard to maintain | Refactor: extract, simplify, SOLID |
| Dead code, debug artifacts | Cleanup: remove, flag uncertain |
| Pre-merge, production prep | Cleanup: lint pass, verify |

## Refactoring Rules

1. **Behavior preserved** - change how, not what
2. **Small steps** - one change, test, commit
3. **Tests essential** - no refactor without tests
4. **Confirm first** - present plan before starting

## Code Smells & Fixes

| Smell | Fix |
|-------|-----|
| Long method (>50 lines) | Extract method |
| Duplicated code | Extract shared function |
| Dead code | Delete (git has history) |
| Magic numbers | Named constants |
| Nested conditionals | Guard clauses |

## Cleanup Quick Reference

| Category | Remove | Flag |
|----------|--------|------|
| Dead code | No refs, commented-out, unreachable | Reflection/dynamic calls |
| Debug | `print()`, `console.log()`, `debugger` | - |
| Imports | Unused | - |
| Comments | Obvious, outdated | "Why" explanations |

## Execution Order

1. Identify candidates
2. Apply file-by-file
3. Run linters (`ruff check --fix`, `eslint --fix`)
4. Verify: tests pass, no regressions

## Security Check

**Verify absent**: Hardcoded credentials, API keys, PII in fixtures
**Verify present**: Env vars for secrets, `.gitignore` entries
