---
description: 'Coding standards for Python, JavaScript/TypeScript, and Rust with shared principles and language-specific best practices'
applyTo: '**/*.py,**/*.js,**/*.mjs,**/*.cjs,**/*.ts,**/*.tsx,**/*.jsx,**/*.rs'
---

# Language Standards

<Goals>

- Type safety: use language-native type systems rigorously
- Fail fast: validate inputs early, specific error types, no silent failures
- Security: no secrets in code, validate at system boundaries
- Performance: avoid O(n^2), batch I/O, profile before optimizing
- Testing: 80% minimum coverage, 95% critical paths, table-driven tests

</Goals>

<Standards>

**Naming**: Descriptive over abbreviated (`getUserById` not `getUsr`), functions <50 lines
**Comments**: Explain "why" not "what"; public APIs must have docs
**Imports**: stdlib > third-party > local (alphabetical within groups)

</Standards>

---

## Python

Toolchain: `ruff` (check+format) | `mypy --strict` | `pytest` | `uv`

<WhatToAdd>

- Type annotations on all functions (parameters + return)
- Google-style docstrings
- `dataclasses(slots=True, frozen=True)` for value objects
- `lru_cache` for expensive computations
- Generators over lists for large datasets
- Precompiled regex, dict/set for O(1) lookups

</WhatToAdd>

```python
from dataclasses import dataclass, field

@dataclass(slots=True, frozen=True)
class User:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)

def process(items: list[str], limit: int = 10) -> dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items[:limit]}
```

```bash
uv sync && uv run pytest -v --cov=src --cov-report=html
```

<Limitations>

- No bare `except:` - catch specific exceptions
- No `Any` without justification
- No global mutable state
- No O(n^2) nested loops for membership testing
- No string formatting in log messages (use field expansion)

</Limitations>

---

## JavaScript/TypeScript

Toolchain: `biome` (zero-config) | `typescript --strict` | `vitest` | `bun`/`pnpm`

<WhatToAdd>

- Strict mode tsconfig (`strict`, `noImplicitAny`, `strictNullChecks`)
- `interface` over `type` for object shapes
- Type guards instead of `as` casts
- `for...of` over `Array.forEach`
- Functional components with hooks (React)
- Custom hooks for reusable logic
- Stable `key` props (not indexes)

</WhatToAdd>

```typescript
interface User {
  id: string;
  name: string;
  roles?: string[];
}

function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

```bash
bun install && bun run test --coverage
```

**Accessibility**: semantic HTML, `htmlFor` on labels, `lang` on `<html>`, no `javascript:` URLs, `tabIndex={0}` for custom interactive elements.

<Limitations>

- No `enum` - use `as const`
- No non-null assertions (`!`) - use type guards
- No `var` - use `const`/`let`
- No `any` without justification
- No `eval()` or dynamic code execution

</Limitations>

---

## Rust

Toolchain: `cargo fmt` | `cargo clippy -- -D warnings` | `cargo test` | `cargo audit`

<WhatToAdd>

- Borrow (`&T`) over ownership when possible
- `Result<T, E>` with `thiserror` for error types
- Traits for abstraction, associated types
- Iterator chains over manual loops
- Stack allocation for small types
- Document `unsafe` blocks

</WhatToAdd>

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Not found: {0}")]
    NotFound(String),
}

pub fn process(input: &str) -> Result<String, AppError> {
    if input.is_empty() {
        return Err(AppError::NotFound("empty input".into()));
    }
    Ok(input.to_uppercase())
}
```

**Smart Pointers**: `Box<T>` (single owner) | `Rc<T>` (shared, single-thread) | `Arc<T>` (shared, thread-safe) | `Mutex<T>`/`RwLock<T>` (interior mutability)

**Concurrency**: channels (`mpsc`) for message passing | `tokio` for async | `rayon` for data parallelism

<Limitations>

- No `.unwrap()` in production
- No panics in library code
- No mutable global state
- No ignoring `Result` types
- No `unsafe` without safety documentation

</Limitations>

---

<Security>

- No hardcoded secrets or credentials
- Input validation at system boundaries only
- Error messages must not leak implementation details
- Audit dependencies regularly
- No sensitive data in logs

</Security>
