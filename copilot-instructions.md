# GitHub Copilot Instructions
> Organization-wide instructions for GitHub Copilot across all Ven0m0 repositories.

---
## Organization Overview
**Ven0m0** builds practical developer tools for automation, platform engineering, and AI-assisted development. This organization values:
<Goals>

- **Readable, self-documenting code** with explicit types and clear names
- **Fast failure** with specific error messages (no silent failures)
- **High test coverage** (80%+ minimum, 95%+ for critical paths)
- **Security by default** (no secrets in code, environment variables for credentials)
- **Conventional commits** (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`)
</Goals>

---
## Core Development Commands
<Commands>

### JavaScript/TypeScript (Node.js with bun)
```bash
# Setup & dependencies
bun install            # Install dependencies
# Development
bun run dev            # Start dev server
bun run build          # Build for production
bun run test           # Run tests
bun run test:watch    # Watch tests
# Quality
bun run lint           # Lint code
bun run format         # Format code
bun run type-check     # TypeScript strict check
bun run build && bun test --coverage
```
### Python (with uv)
```bash
# Setup & dependencies
uv sync                # Install dependencies
uv lock                # Update lock file
uv audit               # Security audit
# Development
uv run python script.py # Run scripts
uv run pytest          # Run tests
uv run pytest -v --cov # Tests with coverage
# Quality
ruff check --fix       # Lint and fix
ruff format            # Format
mypy --strict          # Type check
uv run pytest -v --cov && uv audit
```
### Bash/Shell Scripts
```bash
# Validation / Formatting
shellcheck -s bash -P "SCRIPTDIR" -x -a -o all -S style -f diff script.sh | patch -Np1   # Format with shellcheck
shfmt -i 2 -bn -ci -s -ln bash -w script.sh                                              # Format with shfmt
shellharden --replace script.sh                                                          # Format with shellharden
```
### Rust
```bash
cargo build   # Compile
cargo test    # Run tests
cargo fmt     # Format
cargo clippy  # Lint
cargo audit   # Security audit
```
</Commands>

---
## Code Standards by Language
### JavaScript/TypeScript
- **TypeScript strict mode** (`tsconfig.json`: `"strict": true`, `"noImplicitAny": true`)
- **Types first**: Interfaces over type aliases; type guards instead of `as` casts
- **Naming**: Descriptive over abbreviated; functions < 50 lines
- **React**: Functional components with hooks; stable `key` props (not indexes)
- **Imports**: `stdlib` > `third-party` > `local` (alphabetical within groups)
- **Tool**: `biome` for formatting/linting; `typescript --strict`; `vitest` for tests
**Example**:
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
### Python
- **PEP 8 + PEP 257 (docstrings) + PEP 484 (type hints)**
- **Type annotations**: Full coverage; no `Any` without justification
- **Modern generics**: `list[str]` not `List[str]`; `str | None` not `Optional[str]`
- **Patterns**: Generators over lists; `pathlib` over `os.path`; f-strings
- **Tool**: `ruff` for lint/format; `mypy --strict` for types; `pytest` for tests
**Example**:
```python
from typing import Protocol, TypeVar
Entity = TypeVar("Entity")
class Repository(Protocol):
    def get(self, id: str) -> Entity | None: ...
    def save(self, entity: Entity) -> None: ...
def stream_file(path: str) -> Iterator[str]:
    with open(path) as f:
        yield from f
```
### Bash/Shell
- **Safety first**: `set -euo pipefail`, quote variables, `[[ ]]` not `[ ]`
- **Performance**: Minimize forks, use builtins, batch operations
- **Portability**: POSIX where possible; document OS requirements
- **Clarity**: Descriptive names, explain non-obvious logic
- **Tool**: `shellcheck`, `shfmt`, `shellharden`, use `rg`/`fd` over `grep`/`find`

**Template**:
```bash
#!/usr/bin/env bash
set -euo pipefail; shopt -s nullglob globstar
IFS=$'\n\t' LC_ALL=C
has(){ command -v -- "$1" &>/dev/null; }
die(){ printf '%s\n' "$1" >&2; exit "${2:-1}"; }
main(){
  # Implementation
}
main "$@"
```
### Rust
- **Idiomatic patterns**: Follow Rust conventions
- **Ownership**: Owned by default; borrow when needed
- **Tool**: `cargo fmt`, `cargo clippy`, `cargo audit`

---
## Testing Standards
<Standards>

### Coverage Requirements
- **80% minimum** for all code
- **95% minimum** for critical paths (auth, payment, core logic)
- **Unit tests** for logic isolation
- **Integration tests** for component interaction
- **E2E tests** for critical workflows (where applicable)
</Standards>

### Running Tests
```bash
# JavaScript/TypeScript
bun run test --coverage      # with coverage report
bun run test:watch           # watch mode
# Python
uv run pytest -v --cov       # verbose with coverage
uv run pytest -v --cov --cov-report=html
# Rust
cargo test                   # all tests
cargo test --doc             # doc tests
```

---
## Security Standards
<Security>

### Code Security
- **No hardcoded secrets**: Use environment variables, GitHub Secrets
- **Input validation**: Validate at system boundaries (user input, external APIs)
- **Dependency audit**: `uv audit` (Python), `bun audit` (JavaScript)
- **No generic error handling**: Catch specific exceptions; include context
- **No code generation without matching tests**
### CI/CD Security
- **Action pinning**: Use version tags (e.g., `actions/checkout@v6`), not branches
- **Permissions**: Explicit `permissions:` block, `contents: read` default
- **OIDC**: Short-lived credentials over static secrets
- **Scanning**: CodeQL, dependency review, secret scanning enabled
- **Inputs**: Validate all `workflow_dispatch` inputs
</Security>

---
## Git & Commit Conventions
### Branch Strategy
- **Feature branches**: `feature/description` or `fix/description`
- **Base**: Always branch from `main`
- **Naming**: Lowercase, hyphens, descriptive

### Commit Format
```
<type>(<scope>): <subject>
<body (optional)>
```
**Types**:
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation
- `style` — Formatting (no behavior change)
- `refactor` — Code restructuring (no behavior change)
- `perf` — Performance improvement
- `test` — Test changes
- `chore` — Maintenance, dependencies

**Examples**:
```
feat(agents): add debug agent for application troubleshooting
fix(workflows): correct Python test coverage threshold detection
docs(README): add quick-start installation section
refactor(skills): consolidate code-maintenance patterns
```
### Pull Requests
- **Title**: Same format as commit
- **Description**: What + Why + How to test
- **Size**: ~400 lines of code or less (split large PRs)
- **Approval**: Minimum 1 maintainer review
- **Merge**: Squash commits or rebase-merge for clean history
---
## Tooling Preferences
<Tooling>

### All Platforms (Windows/Mac/Linux)
| Task | Preferred | Fallback |
|------|-----------|----------|
| Search | `rg` (ripgrep) | `grep` |
| Find files | `fd` | `find` |
| JSON/YAML | `jq`/`yq` | - |
| Stream edit | `sd` | `sed` |
| Download | `aria2c` | `curl` |
| List | `eza` | `ls` |
| View | `bat` | `cat` |
### Language-Specific
| Language | Dev Tool | Package Mgr | Linter | Formatter | Type Check | Test |
|----------|----------|------------|--------|-----------|------------|------|
| **JavaScript/TypeScript** | `bun` (runner) | `bun` | `biome` | `biome` | `typescript --strict` | `vitest` |
| **Python** | `uv run` | `uv` | `ruff` | `ruff format` | `mypy --strict` | `pytest` |
| **Bash** | - | - | `shellcheck` | `shfmt` | - | - |
| **Rust** | `cargo` | `cargo` | `clippy` | `cargo fmt` | - | `cargo test` |
Use newer/faster/better tools when possible. Always search for the available mcp servers and tools before starting work. Use tools and skills whenever you can.
</tooling>

---
## Code Review Checklist

<code-review>
  
### Before Submitting a PR
- [ ] Code runs and builds without errors
- [ ] Tests pass: `80%+ coverage minimum`
- [ ] Linter passes: `ruff check`, `biome check`, `shellcheck`, `clippy`
- [ ] Types pass: `TypeScript --strict`, `mypy --strict`
- [ ] No hardcoded secrets or sensitive data
- [ ] Commit messages follow convention
- [ ] Documentation updated (README, API docs, CHANGELOG if applicable)
### When Reviewing
1. **Correctness**: Does it do what it claims?
2. **Security**: No secrets, input validation, dependency audit
3. **Tests**: Adequate coverage; edge cases handled
4. **Performance**: No O(n²) where O(n) works; caching for repeated calls
5. **Clarity**: Readable, self-documenting, follows language standards
6. **Maintainability**: Not over-engineered; no premature optimization
</code-review>

---
## Common Workflows
### New Feature
1. **Plan**: Read relevant instruction files
2. **Branch**: `git checkout -b feature/name`
3. **Implement**: Small commits; pass linters and tests
4. **Test**: 80%+ coverage; all edge cases
5. **Document**: Update README, API docs as needed
6. **PR**: Submit for review; wait for approval
7. **Merge**: Squash commits; use conventional message
### Bug Fix
1. **Understand**: Reproduce the bug; write failing test
2. **Fix**: Implement fix; test passes
3. **Verify**: No regressions; affected tests updated
4. **Commit**: `fix(scope): description`
5. **PR**: Include reproduction steps and test output
### Dependency Update
- **Automated**: Dependabot PRs (auto-merge on success)
- **Manual**: `uv lock` (Python), `bun update` (Node)
- **Audit**: Always run `uv audit` / `bun audit` after updates
- **Test**: Full test suite must pass

---
## Domain-to-Skill Mapping
When working on a task, read the relevant skill module(s) first:
| Task Domain | Relevant Skills |
|-------------|-----------------|
| Feature building | `app-builder/`, `agent-patterns/` |
| Code quality | `code-maintenance/`, `code-review/`, `clean-code/` |
| Testing | `lint-and-validate/` |
| Frontend/React | `nextjs-best-practices/`, `nodejs-best-practices/` |
| API/Backend | `nodejs-best-practices/` |
| Docker/Deploy | `docker-expert/`, `workflow-development/` |
| Git operations | `gh-cli/` |
| Documentation | `docs-writer/`, `documentation-templates/` |
| Performance | App architecture review; profile first |
| Optimization | `language-optimization/` |

**Rule**: Determine domain first → read 1–3 most relevant skill files → apply patterns. @copilot-context-mode-instructions.md

---

## Limitations & Rules

<Limitations>

- **No hardcoded secrets**: Never commit API keys, passwords, tokens
- **No `any` types**: Use type guards or explicit typing instead
- **No generic catch**: Specific exceptions with context
- **No code generation without tests**: Every generated line needs a test
- **No undocumented public APIs**: Docstrings required for public methods
- **No skip/xdescribe**: Don't commit skipped tests
- **No TODO comments**: Create issues instead
- **No large PRs**: Split into logical, reviewable chunks (< 400 LOC)
</Limitations>

---
## Quick Help
**Something not clear?** Check these resources:
- **Language standards**: `instructions/<language>.instructions.md`
- **Domain knowledge**: `skills/<domain>/SKILL.md`
- **CI/CD patterns**: `instructions/cicd-standards.instructions.md`
- **Code review rubric**: `instructions/quality-standards.instructions.md`
- **Git workflows**: `skills/gh-cli/SKILL.md`
- **All instructions**: `instructions/INDEX.md`

---
**Organization**: Ven0m0
**See Also**: `AGENTS.md`/@AGENTS.md,`CLAUDE.md`/@CLAUDE.md
