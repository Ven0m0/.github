# Language Standards

Comprehensive standards for Python, JavaScript/TypeScript, and Rust projects. Each language section builds on shared principles while respecting language-specific idioms and best practices.

## Shared Principles Across All Languages

### Code Quality Standards

1. **Type Safety First**: Use language-native type systems rigorously
   - Eliminate ambiguous types and unsafe casts
   - Leverage compiler/type checker to catch errors early
   - Document unsafe operations explicitly

2. **Fail Fast with Clarity**: Validate inputs early with specific error messages
   - No silent failures or generic errors
   - Explicit error types/enums over broad exception classes
   - Input validation at system boundaries only

3. **Security by Default**: Never commit secrets or credentials
   - Use environment variables for all sensitive configuration
   - Validate inputs at system boundaries (user input, external APIs)
   - No hardcoded credentials, API keys, or database passwords

4. **Performance Mindset**: Build with efficiency awareness
   - Avoid O(n²) algorithms; O(n) is the baseline
   - Batch I/O operations; minimize syscalls
   - Profile before optimizing; measure improvements

5. **Testing Discipline**: Comprehensive coverage with purpose
   - Minimum 80% code coverage; 95% for critical paths
   - Test edge cases, error paths, and boundary conditions
   - Table-driven/parameterized tests for multiple scenarios

### Naming and Readability

- **Descriptive over abbreviated**: `getUserById` not `getUsr`
- **Clear intent**: Names should express purpose without reading implementation
- **Consistency**: Follow language conventions and project patterns
- **Functions**: Small, single responsibility, <50 lines target

### Comments and Documentation

- Explain the **why**, not the **what** — code should be self-documenting
- Complex algorithms need explanatory comments
- Public APIs must have documentation
- No obvious comments: `x = 5; // set x to 5` is noise

### Imports and Dependencies

Order imports as: **stdlib → third-party → local** (alphabetical within each group)

---

## Python Standards

**File patterns**: `*.py`, `*.pyi`
**Toolchain**: `ruff` (check + format), `mypy --strict`, `pytest`

### Setup and Execution

```bash
# Install and manage with uv
uv sync                    # Install dependencies
uv run python -m myapp     # Run application
uv run pytest -v --cov     # Run tests with coverage
uv audit                   # Check for security issues
```

### Type System

**Mandatory**: All functions must have type annotations (parameters + return).

```python
from typing import Protocol, TypeVar, Generic

T = TypeVar("T")

class Repository(Protocol[T]):
    """Generic repository pattern."""
    def get(self, id: str) -> T | None: ...
    def save(self, entity: T) -> None: ...

def process(items: list[str], limit: int = 10) -> dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items[:limit]}
```

**No `Any` without justification**: Eliminate untyped code paths using `@overload` or `Protocol` for complex cases.

### Code Style

- **PEP 8 + 257**: 80-character line limit (pragmatic exceptions for strings/URLs)
- **4-space indent**: Consistent with PEP 8 and repository standards
- **Google-style docstrings**:

```python
def calculate_discount(
    user: User, total: float, membership: str = "standard"
) -> float:
    """Calculate discount based on membership level.

    Args:
        user: User object with membership info.
        total: Order total amount.
        membership: Membership tier ('standard', 'silver', 'gold').

    Returns:
        Discount amount in dollars.

    Raises:
        ValueError: If total is negative or membership is invalid.
    """
    if total < 0:
        raise ValueError("Total cannot be negative")
    rates = {"standard": 0.0, "silver": 0.1, "gold": 0.2}
    return total * rates.get(membership, 0.0)
```

### Data Structures

**Use dataclasses with `slots=True`** for performance:

```python
from dataclasses import dataclass, field

@dataclass(slots=True, frozen=True)
class User:
    id: str
    name: str
    email: str
    tags: list[str] = field(default_factory=list)

    def display_name(self) -> str:
        """Return formatted display name."""
        return f"{self.name} ({self.email})"
```

### Performance and Optimization

- **Use `lru_cache`** for expensive computations:
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=256)
  def expensive_operation(key: str) -> Result:
      return compute(key)
  ```

- **Generators over lists** for large datasets
- **Precompile regex patterns** (not inline)
- **Dict/set lookups** for O(1) access, never O(n) loops for membership testing

### Testing

```bash
# Run all tests with coverage
uv run pytest -v --cov=src --cov-report=html

# Run specific test file or function
uv run pytest tests/unit/test_user.py::test_create_user -v

# Run with markers
uv run pytest -m "not integration" --cov
```

**Structure**:
- Unit tests in `tests/unit/`
- Integration tests in `tests/integration/`
- Fixtures in `tests/conftest.py`
- Mock external dependencies; test behavior, not implementation

### Forbidden Patterns

- ❌ Bare `except:` — always catch specific exceptions
- ❌ `Any` type without justification
- ❌ Global mutable state
- ❌ Hardcoded secrets in code
- ❌ O(n²) nested loops or repeated substring searches
- ❌ String formatting in log messages (use logging's field expansion)

### Run with Optimization

```bash
python3 -OO -m myapp  # Run with optimizations enabled
```

---

## JavaScript/TypeScript Standards

**File patterns**: `*.js`, `*.jsx`, `*.ts`, `*.tsx`
**Toolchain**: `biome` (zero-config), `typescript --strict`, `vitest`

### Setup and Execution

```bash
# Use bun if available, else pnpm
bun install          # or: pnpm install
bun run dev          # Development
bun run test         # Run tests
bun run lint         # Biome linting
bun run format       # Code formatting
```

### Type System

**Mandatory strict mode**:

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitThis": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

**Use `interface` over `type`** for object shapes:

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  roles?: string[];
}

interface UserService {
  getUser(id: string): Promise<User | null>;
  createUser(data: Partial<User>): Promise<User>;
}

// Use generics for reusability
interface Repository<T> {
  get(id: string): Promise<T | null>;
  save(entity: T): Promise<void>;
}
```

**Avoid `any` and `as` casts** — use type guards instead:

```typescript
// BAD: Type assertion
const value = data as string;

// GOOD: Type guard
function isString(value: unknown): value is string {
  return typeof value === "string";
}
if (isString(value)) {
  console.log(value.length); // Now TypeScript knows it's a string
}
```

### React/JSX Best Practices

- **Always specify `key` props** in iterators (use stable identifiers, not indexes)
- **Don't define components inside components** (causes re-mounts)
- **Use `<>...</>` (Fragment)** instead of `<Fragment>`
- **Functional components with hooks** (no class components)
- **Custom hooks for reusable logic**:

```typescript
function useUserData(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetchUser(userId)
      .then(setUser)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [userId]);

  return { user, loading, error };
}
```

### Code Quality Rules

**Accessibility (a11y)** — 45+ rules enforced:

| Rule | Details |
|------|---------|
| Don't use `accessKey` | Use `onKeyDown` or `onKeyUp` instead |
| No `aria-hidden="true"` on focusable elements | Breaks keyboard navigation |
| Label elements must have text and be associated with inputs | Use `htmlFor` attribute |
| Always include `title` on SVG elements | For tooltips and screen readers |
| Always include `lang` attribute on `<html>` | For screen reader language detection |
| Make interactive role elements focusable | Use `tabIndex={0}` for custom buttons |
| Don't use `javascript:` URLs | Use event handlers instead |
| Use semantic HTML (`<button>`, `<nav>`, `<main>`) | Better for accessibility and SEO |

**Complexity & Performance**:

- Prevent excessive cognitive complexity (target <10)
- Use `for...of` instead of `Array.forEach` for better control flow
- No nested describe() blocks (refactor to separate test files)
- No unnecessary string concatenation (use template literals)
- No unreachable code
- Cache DOM queries outside of tight loops

### Testing

```bash
# Run tests with coverage
bun run test --coverage

# Run specific test file
bun run test math.test.ts

# Watch mode
bun run test --watch
```

**Structure**:
- Test files alongside source: `user.ts` + `user.test.ts`
- Use `describe` blocks for organization
- Test behavior, not implementation details
- Mock external dependencies with `vitest.mock()`

### Forbidden Patterns

- ❌ `enum` — use `as const` instead
- ❌ Non-null assertions (`!`) — use type guards
- ❌ `var` — always use `const`/`let`
- ❌ Hardcoded API keys or credentials
- ❌ `eval()` or dynamic code execution
- ❌ `any` type without justification

---

## Rust Standards

**File patterns**: `*.rs`, `Cargo.toml`, `build.rs`
**Toolchain**: `cargo fmt`, `cargo clippy -- -D warnings`, `cargo test`, `cargo audit`

### Core Principles

1. **Ownership and Borrowing**: The foundation of Rust's safety
   - Prefer borrowing (`&T`) over ownership (`T`)
   - Use mutable borrowing (`&mut T`) only when necessary
   - Never clone excessively; borrow instead

```rust
// GOOD: Borrow the string
fn process(data: &str) -> usize {
    data.len()
}

// BAD: Unnecessary cloning
fn process_clone(data: String) -> usize {
    data.len()
}

// GOOD: Mutable borrow when needed
fn modify(data: &mut Vec<i32>) {
    data.push(42);
}
```

2. **Error Handling with `Result<T, E>`**: No `.unwrap()` in production
   - Use `thiserror` crate for error types
   - Return `Result` from fallible functions
   - Implement error context with `?` operator

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Parse error: {0}")]
    Parse(#[from] serde_json::Error),
    #[error("User not found: {0}")]
    NotFound(String),
}

pub type Result<T> = std::result::Result<T, AppError>;

pub fn load_config(path: &str) -> Result<Config> {
    let contents = std::fs::read_to_string(path)?;
    let config = serde_json::from_str(&contents)?;
    Ok(config)
}
```

### Type System and Traits

**Use traits for abstraction**:

```rust
pub trait Repository<T> {
    fn get(&self, id: &str) -> std::result::Result<T, Error>;
    fn save(&mut self, entity: T) -> std::result::Result<(), Error>;
}

pub trait Processor {
    type Output;
    fn process(&self, input: &str) -> Self::Output;
}

impl Processor for JsonProcessor {
    type Output = serde_json::Value;
    fn process(&self, input: &str) -> Self::Output {
        serde_json::from_str(input).unwrap_or_default()
    }
}
```

**Lifetimes and Generics**:

```rust
// Generic constraint with lifetime
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
}

// Associated types reduce complexity
trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}
```

### Smart Pointers

Use appropriate pointer types for different ownership scenarios:

| Type | Use Case |
|------|----------|
| `Box<T>` | Heap allocation, single owner |
| `Rc<T>` | Multiple immutable owners (single-threaded) |
| `Arc<T>` | Multiple immutable owners (thread-safe) |
| `RefCell<T>` | Interior mutability (single-threaded) |
| `Mutex<T>` | Thread-safe interior mutability |
| `RwLock<T>` | Multiple readers, single writer |

```rust
use std::sync::{Arc, Mutex};
use std::rc::Rc;

// Single-threaded shared state
let data = Rc::new(vec![1, 2, 3]);
let clone1 = Rc::clone(&data);

// Thread-safe shared state
let shared = Arc::new(Mutex::new(vec![1, 2, 3]));
let clone2 = Arc::clone(&shared);
```

### Performance Optimization

**Iterators over loops**:

```rust
// GOOD: Iterator chain
let result: Vec<i32> = data.iter()
    .filter(|x| x > &&5)
    .map(|x| x * 2)
    .collect();

// BAD: Manual loop
let mut result = Vec::new();
for x in &data {
    if x > &5 {
        result.push(x * 2);
    }
}
```

**Stack over heap** — use stack for small types:

```rust
// GOOD: Stack allocation
let nums = [1, 2, 3, 4, 5];

// Acceptable: Heap when necessary
let large = Box::new(vec![0; 1_000_000]);
```

**Inline hints** (use judiciously, measure):

```rust
#[inline]
fn simple_add(a: i32, b: i32) -> i32 {
    a + b
}

#[inline(never)]
fn expensive_operation() -> Result<Data> {
    // Complex logic
}
```

### Code Style

- **Format with `cargo fmt`**: Non-negotiable
- **Max line length**: 100 characters (pragmatic exceptions)
- **Clippy strict**: `cargo clippy -- -D warnings` must pass
- **No unsafe blocks** without documentation:

```rust
/// SAFETY: This assumes the pointer is valid and points to initialized memory
/// that lives for at least 'a.
unsafe fn dereference<'a>(ptr: *const T) -> &'a T {
    &*ptr
}
```

### Testing and Documentation

```bash
# Run all tests
cargo test

# Test with output
cargo test -- --nocapture

# Test specific module
cargo test module_name

# Benchmark
cargo bench
```

**Documentation**:

```rust
/// Processes data and returns a result.
///
/// # Arguments
///
/// * `input` - The input data to process
///
/// # Returns
///
/// Returns a Result containing the processed data or an error.
///
/// # Errors
///
/// Returns `AppError::InvalidInput` if the input is malformed.
///
/// # Examples
///
/// ```
/// let result = process("data")?;
/// assert_eq!(result, "DATA");
/// # Ok::<(), Box<dyn std::error::Error>>(())
/// ```
pub fn process(input: &str) -> Result<String> {
    if input.is_empty() {
        return Err(AppError::InvalidInput("empty input".into()));
    }
    Ok(input.to_uppercase())
}
```

### Concurrency

**Channels for message passing**:

```rust
use std::sync::mpsc;
use std::thread;

let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    tx.send(42).unwrap();
});
let received = rx.recv().unwrap();
```

**Async/await with Tokio**:

```rust
use tokio::task;

#[tokio::main]
async fn main() {
    let handle = task::spawn(async { 42 });
    let result = handle.await.unwrap();
}
```

**Rayon for data parallelism**:

```rust
use rayon::prelude::*;

let result: Vec<i32> = data
    .par_iter()
    .map(|x| expensive_operation(x))
    .collect();
```

### Forbidden Patterns

- ❌ `.unwrap()` in production code
- ❌ Panic in library code
- ❌ Mutable global state
- ❌ Hardcoded credentials
- ❌ Ignoring `Result` types
- ❌ Unsafe code without documentation

---

## Cross-Language Patterns

### Configuration Management

All languages: Use environment variables for runtime config, structured files (YAML/TOML) for complex settings, validate at startup.

### Security Checklist

- [ ] No hardcoded secrets
- [ ] Input validation at system boundaries
- [ ] Error messages don't leak implementation details
- [ ] Dependencies audited regularly
- [ ] Logging doesn't include sensitive data

### Error Handling Pattern

Across all languages: Specific error types, context when wrapping errors, consistent error messages.

---

## Additional Resources

- **Python**: PEP 8, PEP 257, PEP 484 (type hints), Real Python guides
- **JavaScript/TypeScript**: TypeScript Handbook, MDN Web Docs, React documentation, Biome docs
- **Rust**: The Rust Book, Rustonomicon, Clippy lints, error-handling best practices

