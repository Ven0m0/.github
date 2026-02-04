# Code Quality and Performance Standards

Standards for code review methodology, quality assessment, and performance optimization across all projects.

## Code Review Standards

Code reviews ensure quality, knowledge sharing, and early detection of issues. This document provides systematic review methodology and standards.

### Review Scope and Focus

**Code reviews should evaluate**:

- **Correctness**: Does the code do what it's supposed to do?
- **Clarity**: Is the code easy to understand?
- **Maintainability**: Can someone else (or you, 6 months later) maintain this?
- **Security**: Are there potential vulnerabilities?
- **Performance**: Does it perform acceptably?
- **Test Coverage**: Are the changes properly tested?
- **Documentation**: Are changes documented appropriately?

**Code reviews should NOT**:

- Enforce personal coding style preferences without foundation
- Require perfection (better is the enemy of done)
- Become adversarial — focus on the code, not the person
- Request features beyond the scope of the PR

### Review Methodology

#### Step 1: Understand the Context

1. Read the PR title and description
2. Understand what problem is being solved
3. Review linked issues for requirements
4. Check if this is a breaking change
5. Verify the scope matches the description

#### Step 2: Examine Code Changes Systematically

1. **Start with the broadest view**: File structure, architecture
2. **Zoom in**: Module organization, class/function design
3. **Review logic**: Implementation details, error handling
4. **Check details**: Naming, formatting, comments

#### Step 3: Apply Domain-Specific Standards

Review against language-specific standards:
- See: `lang-standards.instructions.md` (Python, JavaScript, Rust)
- See: `shell-standards.instructions.md` (Shell scripting)
- See: `cicd-standards.instructions.md` (Workflows and CI/CD)

#### Step 4: Security Review

Apply security checklist:

- [ ] No hardcoded credentials, API keys, or secrets
- [ ] Input validation at system boundaries
- [ ] Proper error handling without information disclosure
- [ ] Dependencies are trusted and up-to-date
- [ ] Sensitive operations are properly authenticated/authorized
- [ ] Data is encrypted in transit and at rest if required
- [ ] No use of insecure cryptographic algorithms
- [ ] Log outputs don't contain sensitive information
- [ ] Third-party libraries checked for known vulnerabilities

#### Step 5: Verify Tests

- [ ] All public methods/functions have tests
- [ ] Edge cases are covered (null, empty, boundary conditions)
- [ ] Error paths are tested
- [ ] Integration tests exist for critical flows
- [ ] Coverage thresholds are met (80%+ minimum, 95%+ for critical)

#### Step 6: Performance Considerations

Check for:

- [ ] O(n²) or worse algorithms where O(n) is viable
- [ ] Unnecessary data copies or clones
- [ ] Repeated external API calls that could be cached
- [ ] Missing database indices or query optimization
- [ ] Unbounded collections that could cause memory issues
- [ ] Blocking operations in async contexts

### Review Comment Standards

**Provide constructive feedback**:

```
❌ BAD: "This code is wrong"
✅ GOOD: "This could cause a race condition when used in concurrent scenarios.
           Consider using a lock or atomic operations."

❌ BAD: "Why would you do it this way?"
✅ GOOD: "Have you considered using a Strategy pattern here instead? It would
           make it easier to add new implementations without modifying existing code."

❌ BAD: "This doesn't match the style guide"
✅ GOOD: "Following our Python standards (see lang-standards.md), we should use
           f-strings instead of .format() for string interpolation."
```

**Use conventional prefixes**:

- `MUST`: Critical issue that blocks approval
- `SHOULD`: Strong recommendation; likely approval-blocking
- `CONSIDER`: Suggestion for improvement; doesn't block approval
- `QUESTION`: Seeking clarification
- `NITPICK`: Minor style/formatting issue

### Approval and Merge Criteria

**Approve when**:

- All critical issues (`MUST`) are addressed
- All strong recommendations (`SHOULD`) are addressed or explicitly rejected with rationale
- Tests are comprehensive and passing
- Security review passes
- Code follows project standards
- Documentation is updated

**Do not approve when**:

- Failing tests
- Critical security issues
- No test coverage for new code
- Breaking changes without CHANGELOG update
- Undocumented APIs or significant behavior changes

---

## Performance Optimization Standards

### Performance Mindset

1. **Measure Before Optimizing**: Profile to identify actual bottlenecks
2. **Know the Constraints**: What are acceptable latency/throughput/memory targets?
3. **Optimize Where It Matters**: Focus on hot paths, not edge cases
4. **Document Trade-offs**: Performance improvements often have maintainability costs
5. **Verify Improvements**: Measure again after optimization

### Profiling and Analysis

**Identify bottlenecks using language-specific tools**:

**Python**:
```python
import cProfile
import pstats

cProfile.run('main()', 'stats')
p = pstats.Stats('stats')
p.sort_stats('cumulative').print_stats(10)
```

**JavaScript**:
```javascript
console.time('operation');
// ... code to measure ...
console.timeEnd('operation');

// Browser: DevTools → Performance tab
// Node: node --prof app.js
```

**Rust**:
```bash
cargo build --release
cargo bench
cargo asm function_name
```

### Common Performance Issues

#### 1. Algorithm Complexity

**Problem**: O(n²) where O(n) is possible

```python
# BAD: O(n²) nested loop searching
result = []
for item in items:
    for search_item in items:
        if item == search_item:
            result.append(item)

# GOOD: O(n) using set
item_set = set(items)
result = list(item_set)
```

**Fix**: Choose appropriate data structures (hash sets for membership testing, etc.)

#### 2. Unnecessary Copies

**Problem**: Creating copies when references suffice

```python
# BAD: Unnecessary list copy
def process(items):
    copy = items[:]  # Unnecessary copy
    return [x * 2 for x in copy]

# GOOD: Use reference
def process(items):
    return [x * 2 for x in items]
```

**Fix**: Use references, generators, views instead of copies

#### 3. Repeated Computation

**Problem**: Computing the same value multiple times

```python
# BAD: Recompute in loop
for item in items:
    if is_valid(item) and is_valid(item):  # Computed twice
        process(item)

# GOOD: Cache result
for item in items:
    if is_valid(item):
        process(item)

# BAD: Expensive operation in loop
for user in users:
    total += expensive_db_query()  # Called for every user

# GOOD: Cache outside loop
totals = {id: expensive_db_query() for id in user_ids}
for user in users:
    total += totals[user.id]
```

**Fix**: Cache results, use memoization, precompute when possible

#### 4. I/O in Hot Paths

**Problem**: Synchronous I/O in loops or frequent operations

```python
# BAD: Database call in loop
for user_id in user_ids:
    user = db.get_user(user_id)  # Blocks for each user
    process(user)

# GOOD: Batch the query
users = db.get_users(user_ids)  # Single database call
for user in users:
    process(user)
```

**Fix**: Batch operations, use async I/O, implement caching

#### 5. String Concatenation

**Problem**: Building strings in loops

```python
# BAD: String concatenation in loop (creates new string each iteration)
result = ""
for item in items:
    result += item  # O(n²) complexity due to string immutability

# GOOD: Use list and join
result = "".join(items)  # O(n) complexity
```

**Fix**: Use StringBuilder pattern (list.join in Python, StringBuffer in Java)

#### 6. Memory Leaks

**Problem**: Holding references to large objects unnecessarily

```python
# BAD: Keep references in global list
cache_list = []
def add_to_cache(large_object):
    cache_list.append(large_object)  # Never removed, grows unbounded

# GOOD: Use LRU cache with maxsize
from functools import lru_cache
@lru_cache(maxsize=128)
def get_value(key):
    return expensive_operation(key)
```

**Fix**: Implement proper cache eviction, use weak references, clean up resources

#### 7. Inefficient Data Structures

**Problem**: Wrong data structure for the use case

| Operation | List | Set | Dict |
|-----------|------|-----|------|
| Contains check | O(n) | O(1) | O(1) |
| Append | O(1) | O(1) | — |
| Insert | O(n) | — | — |
| Lookup | O(n) | — | O(1) |
| Remove | O(n) | O(1) | O(1) |

```python
# BAD: Using list for membership testing
if item in list:  # O(n)
    process(item)

# GOOD: Using set
if item in item_set:  # O(1)
    process(item)
```

**Fix**: Choose appropriate data structures (lists for order, sets for membership, dicts for lookup)

### Optimization Techniques by Language

#### Python

- Use generators for large datasets: `yield` instead of `return list`
- Leverage numpy/pandas for numerical operations
- Use `functools.lru_cache` for expensive computations
- Profile with cProfile before optimizing
- Consider PyPy for CPU-intensive code
- Use `sys.intern()` for repeated strings (rare cases)

#### JavaScript/TypeScript

- Use `requestAnimationFrame` for UI updates
- Implement virtual scrolling for large lists
- Use Web Workers for heavy computation
- Minimize DOM manipulations (batch with DocumentFragment)
- Use event delegation instead of multiple listeners
- Profile with Chrome DevTools Performance tab

#### Rust

- Use iterators instead of manual loops
- Prefer stack allocation over heap when possible
- Use `#[inline]` for small hot-path functions (measure!)
- Implement custom allocators for specific workloads
- Use SIMD for numerical operations
- Profile with `cargo-flamegraph`

### Performance Standards by Use Case

**Web Applications**:

- Page load: < 3 seconds initial load, < 1 second interactive
- UI response: < 100ms for user interactions
- API endpoints: < 200ms p95 latency
- Database queries: < 50ms p95 (excluding complex aggregations)

**CLI Tools**:

- Startup time: < 100ms for small operations
- Per-operation: < 1 second for common operations
- Memory: < 50MB for small tools, < 500MB for large operations

**Libraries**:

- No blocking operations in async APIs
- Minimize allocations in hot paths
- Lazy evaluation where applicable
- Provide performance bounds in documentation

### Documentation Standards for Performance

When code has performance implications, document:

```python
def complex_operation(data: list[int]) -> int:
    """Process data with specific performance characteristics.

    Time Complexity: O(n log n) due to internal sort
    Space Complexity: O(n) for auxiliary data structures

    Note: This operation is suitable for datasets up to ~100K items.
    For larger datasets, consider streaming or incremental approaches.
    """
    # Implementation
```

### Optimization Checklist

- [ ] Identified actual bottleneck (profiled, not guessed)
- [ ] Measured baseline performance
- [ ] Applied optimization
- [ ] Verified improvement with measurements
- [ ] Assessed maintainability trade-offs
- [ ] Added performance documentation
- [ ] Tests still pass
- [ ] Code review completed

---

## Quality Metrics and Standards

### Code Coverage

- **Minimum**: 80% coverage across the codebase
- **Critical paths**: 95%+ coverage (authentication, payments, security)
- **New code**: 90%+ coverage (no regressions)
- **Measurement**: Track coverage trends over time

### Cyclomatic Complexity

- **Target**: < 10 for most functions
- **Maximum**: < 20 before refactoring is mandatory
- **Reduce by**: Extracting methods, using patterns (Strategy, State)

### Code Duplication

- **Dry Principle**: Extract duplicated code into shared utilities
- **Maximum**: < 3% code duplication (project-wide)
- **Tools**: `codecov` reports, `clonedigger`, language-specific analyzers

### Maintainability Index

- **Target**: > 80 (highly maintainable)
- **Acceptable**: 60-80 (moderate, refactor as needed)
- **Poor**: < 60 (refactor before adding features)

### Technical Debt

Track and address:

- [ ] FIXME comments with context and timeline
- [ ] TODO items with resolution plans
- [ ] Deprecated code with migration paths
- [ ] Legacy patterns preventing modern features

---

## Quality Gates for Production

All PRs must satisfy:

- ✅ All tests passing
- ✅ Code coverage >= 80%
- ✅ No security vulnerabilities (per audit tools)
- ✅ Linting passes (language-specific rules)
- ✅ Type checking passes (strict mode)
- ✅ No unresolved review comments
- ✅ Documentation updated
- ✅ Performance acceptable (no regressions)

---

## References

- **Code Review Best Practices**: Google's Code Review Developer Guide
- **Performance Optimization**: Language-specific profiling and optimization guides
- **Quality Metrics**: SonarQube Quality Gates, Codeclimate standards
- **Security Review**: OWASP Top 10, CWE/SANS Top 25

