---
name: language-optimization
description: Common patterns and principles for code optimization across languages. Use when asked to improve readability, performance, maintainability, or security in Bash, Python, or Rust code.
version: 1.0.0
allowed-tools: [Read, Glob, Grep]
---

# Language Optimization Skill

Common patterns, principles, and workflows for optimizing code across different programming languages.

## Universal Optimization Principles

### KISS (Keep It Simple, Stupid)
- Simple over clever
- Readability first
- Clear variable names
- Self-documenting code
- Avoid unnecessary complexity

### YAGNI (You Aren't Gonna Need It)
- Don't build before needed
- No premature optimization
- Profile before optimizing
- Solve current problems, not hypothetical ones

### DRY (Don't Repeat Yourself)
- Extract repeated logic
- Create reusable functions/modules
- Single source of truth
- Consolidate duplicate code

### Fail Fast
- Validate early in execution
- Specific error messages
- Comprehensive error handling
- Clear failure modes

### Security First
- No secrets in code
- Validate at boundaries (user input, external APIs)
- Principle of least privilege
- Regular security audits
- Input sanitization

## Common Workflow Pattern

All language optimizers follow this pattern:

1. **Analyze**: Examine code for issues, performance bottlenecks, security vulnerabilities
2. **Lint/Format**: Apply language-specific linters and formatters
3. **Type Check**: Enforce type safety (where applicable)
4. **Test**: Ensure comprehensive test coverage
5. **Optimize**: Apply performance improvements based on profiling
6. **Verify**: Run all tests and checks to ensure correctness

## Tool Selection Strategy

### Analysis Tools
- Static analysis for code quality
- Profilers for performance bottlenecks
- Security scanners for vulnerabilities
- Type checkers for type safety

### Linters
- Language-specific linters for code quality
- Auto-fix where possible
- Enforce consistent style

### Formatters
- Automated code formatting
- Consistent indentation and spacing
- Remove formatting debates

### Testing
- Unit tests for individual functions
- Integration tests for components
- Coverage reports for completeness
- Test-driven development (TDD)

## Performance Optimization Patterns

### Before Optimizing
1. **Profile first**: Measure before optimizing
2. **Identify bottlenecks**: Focus on slowest parts
3. **Set benchmarks**: Establish baseline performance

### Common Optimizations
- **Algorithm complexity**: O(n²) → O(n) or O(log n)
- **Caching**: Memoize expensive computations
- **Lazy evaluation**: Compute only when needed
- **Batching**: Group operations to reduce overhead
- **Prefer built-ins**: Use optimized standard library functions

### After Optimizing
1. **Verify correctness**: All tests still pass
2. **Measure improvement**: Compare to baseline
3. **Document trade-offs**: Note any complexity added

## Security Patterns

### Input Validation
- Validate all user input
- Sanitize before use
- Use allowlists, not blocklists
- Validate type, format, range

### Secret Management
- Never commit secrets to code
- Use environment variables
- Use secret management systems
- Rotate credentials regularly

### Dependency Security
- Regular security audits
- Keep dependencies updated
- Use vulnerability scanners
- Pin versions for reproducibility

## Code Quality Metrics

### Maintainability
- Cyclomatic complexity: Lower is better
- Function length: Shorter is better
- Nesting depth: Shallower is better
- Code duplication: Less is better

### Test Coverage
- Aim for 90%+ line coverage
- 100% critical path coverage
- Test edge cases
- Test error handling

### Type Safety
- Strong typing where available
- Explicit type annotations
- No implicit any/dynamic types
- Type-driven development

## Error Handling Patterns

### Best Practices
- Use language-specific error types (Result, Either, exceptions)
- Catch specific exceptions, not generic
- Provide context in error messages
- Log errors with sufficient detail
- Never silently fail

### Error Messages
- Clear description of what failed
- Context about where it failed
- Guidance on how to fix
- Include relevant values

## Testing Patterns

### Test-Driven Development (TDD)
1. Write failing test
2. Write minimal code to pass
3. Refactor while keeping tests green

### Test Organization
- Arrange-Act-Assert pattern
- One assertion per test (where possible)
- Clear test names describing behavior
- Test both happy path and edge cases

### Test Types
- **Unit tests**: Individual functions/methods
- **Integration tests**: Component interactions
- **Property-based tests**: Generate test cases
- **Regression tests**: Prevent known bugs

## Refactoring Patterns

### When to Refactor
- Code smells identified
- Before adding new features
- After fixing bugs
- During code review

### Common Refactorings
- **Extract function**: Pull out repeated code
- **Rename**: Clarify intent
- **Simplify conditionals**: Reduce nesting
- **Remove dead code**: Delete unused code
- **Introduce types**: Add type safety

### Refactoring Safety
- Always have tests first
- Small, incremental changes
- Run tests after each step
- Use automated refactoring tools

## Language-Specific Adaptations

Each language has specific implementations of these patterns:

### Bash/Shell
- Focus on quoting, error handling (set -euo pipefail)
- Prefer modern tools (fd, rg over find, grep)
- Use shellcheck, shellharden
- See: `instructions/bash.instructions.md`

### Python
- Focus on type hints, async patterns
- Use ruff for linting, mypy for types
- Prefer generators over lists
- See: `instructions/python.instructions.md`

### Rust
- Focus on ownership, borrowing, lifetimes
- Use clippy for lints, rustfmt for formatting
- Prefer iterators over loops
- See: `instructions/rust.instructions.md`

## Success Criteria

Optimization is successful when:
- ✅ All tests pass
- ✅ Code quality metrics improved
- ✅ Performance improved (measured)
- ✅ Security vulnerabilities addressed
- ✅ Type safety enforced
- ✅ Code follows language idioms
- ✅ Maintainability improved

## Anti-Patterns to Avoid

- Premature optimization without profiling
- Sacrificing readability for minor performance gains
- Over-engineering simple solutions
- Ignoring test failures
- Skipping type safety for convenience
- Committing secrets or sensitive data
- Copy-pasting code instead of extracting functions
- Optimizing for hypothetical future requirements

## References

- Language-specific standards in `instructions/`
- Refactoring patterns in `skills/refactor/`
- Code cleanup procedures in `skills/codebase-cleanup/`
