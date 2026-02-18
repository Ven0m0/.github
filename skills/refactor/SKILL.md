---
name: refactor
description: 'Surgical code refactoring to improve maintainability without changing behavior. Covers extracting functions, eliminating code smells, and applying design patterns. Use for gradual improvements.'
user-invocable: true
disable-model-invocation: false
---

# Refactor

Improve code structure and readability without changing external behavior. Gradual evolution, not revolution.

## When to Use

- Code is hard to understand or maintain
- Functions/classes are too large
- Code smells need addressing
- Adding features is difficult due to structure

## Golden Rules

1. **Behavior is preserved** - only change how, not what
2. **Small steps** - tiny changes, test after each
3. **Tests are essential** - without tests, you're just editing
4. **One thing at a time** - don't mix refactoring with features
5. **Version control** - commit before and after each safe state

## Code Smells & Fixes

| Smell | Fix |
|-------|-----|
| Long method (>50 lines) | Extract method - break into focused functions |
| Duplicated code | Extract common logic into shared function |
| Large class/module | Split by responsibility (SRP) |
| Long parameter list | Group into parameter object or builder |
| Feature envy | Move logic to the object that owns the data |
| Primitive obsession | Create domain types (Email, PhoneNumber) |
| Magic numbers/strings | Named constants |
| Nested conditionals | Guard clauses / early returns |
| Dead code | Delete it (git has history) |
| Inappropriate intimacy | Ask, don't tell - encapsulate access |

## Common Operations

| Operation | Description |
|-----------|-------------|
| Extract Method | Turn code fragment into method |
| Extract Class | Move behavior to new class |
| Extract Interface | Create interface from implementation |
| Inline Method/Class | Move body back to caller |
| Introduce Parameter Object | Group related parameters |
| Replace Conditional with Polymorphism | Strategy pattern |
| Replace Magic Number with Constant | Named constants |
| Decompose Conditional | Break complex conditions |
| Replace Nested Conditional with Guard Clauses | Early returns |

## Design Patterns for Refactoring

- **Strategy**: Replace switch/if chains with polymorphic strategies
- **Chain of Responsibility**: Replace nested validation with composable validators
- **Builder**: Replace long constructors/parameter lists

## Safe Process

```
1. PREPARE: Ensure tests exist, commit current state, create branch
2. IDENTIFY: Find smell, understand code, plan refactoring
3. REFACTOR: One small change -> run tests -> commit -> repeat
4. VERIFY: All tests pass, performance unchanged or improved
5. CLEAN UP: Update comments and documentation
```

## Checklist

- [ ] Functions are small (<50 lines) and do one thing
- [ ] No duplicated code
- [ ] Descriptive names (variables, functions, classes)
- [ ] No magic numbers/strings
- [ ] Dead code removed
- [ ] Clear module boundaries, no circular dependencies
- [ ] Types defined for public APIs, no unjustified `any`
- [ ] All tests pass
