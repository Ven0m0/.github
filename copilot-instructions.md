# GitHub Copilot Instructions

> Organization-wide instructions for GitHub Copilot across all Ven0m0 repositories

<HighLevelDetails>

**Ven0m0** builds practical open source tools for developer workflows, platform engineering, automation, and AI-assisted development.

</HighLevelDetails>

<Goals>

- Readable, self-documenting code with explicit types and clear names
- Fail fast with specific error messages; no silent failures
- 80%+ test coverage; 95% for critical paths
- Security by default: no secrets in code, environment variables for credentials
- Conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`

</Goals>

<Limitations>

- No hardcoded secrets, API keys, or credentials
- No generic error handling (catch specific exceptions)
- No `any` types without justification
- No code generation without matching tests
- No undocumented public APIs

</Limitations>

## Language Standards

### Python

Tech: Python 3.14+ | `uv` (packages) | `ruff` (lint+format) | `basedpyright` (types) | `pytest`

```python
def process_data(items: list[str], limit: int = 10) -> dict[str, int]:
    """Process items and return counts."""
    ...
```

- Google-style docstrings, type annotations mandatory
- `dataclasses` or `pydantic` for data structures
- Layout: `src/package_name/`, `tests/{unit,integration}/`, `pyproject.toml`

### TypeScript/JavaScript

Tech: Node.js 25+ ESM | `bun` (if `bun.lockb`/`bunfig.toml`) else `pnpm` | `biome` | `vitest`

```typescript
interface UserConfig {
  name: string;
  timeout?: number;
}
export function createClient(config: UserConfig): Client { ... }
```

- Strict mode, `interface` over `type` for objects, no `enum` (use `as const`)
- Layout: `src/`, `tests/`, `package.json`, `tsconfig.json`

### Rust

Tech: Latest stable | `clippy` pedantic | `cargo-deny` | `thiserror`

```rust
pub fn process(input: &str) -> Result<Output, Error> { ... }
```

- Document all public items with examples
- No `.unwrap()` in production

### Java

Tech: Java 25 | Spring Boot 3.3+ | Gradle Kotlin DSL | Checkstyle Google

- Constructor injection, Records for DTOs

## Cross-Language Patterns

<Standards>

**Error Handling**: Specific error types, context when wrapping, explicit messages

```python
msg = f"Failed to process {item}: {reason}"
raise ValueError(msg)
```

```go
return fmt.Errorf("failed to fetch user %s: %w", id, err)
```

**Testing**: Table-driven tests, mock externals, test edge cases and error paths

**Config**: Environment variables for runtime, YAML/TOML for complex settings, validate at startup

**Imports**: stdlib > third-party > local (alphabetical within groups)
</Standards>

<Security>

1. Environment variables or secret managers for credentials
2. Dependabot enabled, review CVEs
3. SHA-pinned Actions (commit SHA; minimum: major version tag)
4. GITHUB_TOKEN with least privilege
5. Pre-commit hooks with gitleaks
</Security>

## CI/CD

Reusable workflows in `.github/workflows/`: `comprehensive-lint.yml`, `bun.yml`, `uv-lock.yml`, `dependabot-automerge.yml`, `git-maintenance.yml`, `img-opt.yml`

<WhatToAdd>

When generating code:
1. Match existing style in surrounding code
2. Include tests alongside implementation
3. Add docstrings/comments for complex logic
4. Include proper error handling
5. Account for null, empty, and boundary conditions
</WhatToAdd>

## AI Assistant Integration

| File | Contents |
|------|----------|
| `AGENTS.md`/`CLAUDE.md` | Overview, structure, build/test commands, style requirements |
| `.vscode/mcp.json` | context7, filesystem, memory (when applicable), serena, github-mcp, exa |
