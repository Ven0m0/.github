---
description: "Refactor and optimize Python code following project standards"
agent: "always"
tools: ["read", "edit", "search", "execute"]
---

# Python Refactoring

**Goal**: Refactor existing Python code for maintainability, type safety, and performance while preserving behavior.

Standards: See `instructions/python.instructions.md`

## Key Requirements

- **Toolchain**: `ruff check --fix && ruff format`, `mypy --strict`, `pytest -v --cov`
- **Type Safety**: Full annotations, modern generics (`list[str]`), no `Any`
- **Performance**: O(n) algorithms, `lru_cache`, generators for large data
- **Security**: Input validation, no hardcoded secrets

## High-Performance Libraries

| Standard   | Optimized | Reason                   |
| ---------- | --------- | ------------------------ |
| `json`     | `orjson`  | 6x faster serialization  |
| `asyncio`  | `uvloop`  | Node.js-level event loop |
| `requests` | `httpx`   | Async, HTTP/2 support    |

## Workflow

1. **Plan**: Summarize changes, rationale, verification steps
2. **Refactor**: Incremental, atomic changes
3. **Verify**: Run linters/tests, check metrics
