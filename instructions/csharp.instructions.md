---
applyTo: "**/*.cs,**/*.csproj,**/*.sln"
description: "C# 12/.NET 8: nullable types, async/await, records"
---

# C# Standards

Version: C# 12 / .NET 8

## Toolchain

- **Build**: dotnet CLI or MSBuild
- **Lint**: .NET analyzers, StyleCop
- **Test**: xUnit or NUnit
- **Coverage**: coverlet >= 85%

## Core Rules

**MUST:**
- Use nullable reference types (enable in csproj)
- Use records for immutable data
- Use async/await for I/O operations
- Use primary constructors for simple classes
- Dispose resources with `using` statements
- Document public APIs with XML comments

**MUST NOT:**
- Catch `Exception` without filtering
- Use `async void` (except event handlers)
- Ignore nullable warnings
- Use magic strings for configuration
- Block async code with `.Result` or `.Wait()`
- Store secrets in `appsettings.json`

## File Conventions

- `*Tests.cs` for test files
- One type per file
- PascalCase for public members
- camelCase for private fields (with `_prefix`)
- Match namespace to folder structure

## Testing

- Use xUnit with `[Theory]` for data-driven tests
- Use NSubstitute or Moq for mocking
- Use FluentAssertions for readable assertions
- Use Testcontainers for integration tests
