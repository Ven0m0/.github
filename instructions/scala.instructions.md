---
applyTo: "**/*.scala,**/*.sc,**/build.sbt"
description: "Scala 3.4+: case classes, for-comprehensions, effect types"
---

# Scala Standards

Version: Scala 3.4+

## Toolchain

- **Build**: sbt or Mill
- **Lint**: Scalafix, WartRemover
- **Format**: scalafmt
- **Test**: ScalaTest or MUnit

## Core Rules

**MUST:**
- Use immutable collections by default
- Use case classes for data types
- Use for-comprehensions for monadic operations
- Use extension methods over implicits
- Use `given`/`using` for context parameters
- Handle errors with `Either` or effect types

**MUST NOT:**
- Use `null` (use `Option` instead)
- Use `var` except in performance-critical code
- Use `Any` or `AnyRef` as type bounds
- Throw exceptions for control flow
- Use implicit conversions
- Ignore compiler warnings

## File Conventions

- `*Spec.scala` or `*Test.scala` for test files
- PascalCase for types and objects
- camelCase for values and methods
- Package structure matches directory
- Companion object in same file

## Testing

- Use ScalaTest or MUnit
- Use property-based testing with ScalaCheck
- Use mock libraries sparingly
- Test effect types properly
