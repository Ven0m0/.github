---
applyTo: "**/{*.java,pom.xml,build.gradle,build.gradle.kts}"
---

# Java Standards

Version: Java 21 LTS

## Toolchain

- **Build**: Maven or Gradle
- **Lint**: Checkstyle, SpotBugs
- **Test**: JUnit 5, Mockito
- **Coverage**: JaCoCo >= 85%

## Core Rules

**MUST:**

- Use records for immutable data classes
- Use pattern matching with switch expressions
- Use virtual threads for concurrent I/O operations
- Close resources with try-with-resources
- Use `Optional` for nullable return values
- Document public APIs with Javadoc

**MUST NOT:**

- Use raw types (always parameterize generics)
- Catch `Exception` or `Throwable` (catch specific exceptions)
- Use `null` for empty collections (return empty collection)
- Ignore `InterruptedException`
- Use public fields (use accessors or records)
- Store secrets in source code

## File Conventions

- `*Test.java` for test files
- One public class per file
- Package name matches directory structure
- PascalCase for classes
- camelCase for methods and variables

## Testing

- Use JUnit 5 with `@ParameterizedTest`
- Use Mockito for mocking
- Use AssertJ for fluent assertions
- Use Testcontainers for integration tests
