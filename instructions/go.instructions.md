---
applyTo: "**/*.go,**/go.mod,**/go.sum"
description: "Go 1.23+: error handling, context, golangci-lint"
---

# Go Standards

Version: Go 1.23+

## Toolchain

- **Lint**: golangci-lint
- **Format**: `gofmt`, `goimports`
- **Test**: `go test` with coverage >= 85%
- **Packages**: go modules

## Core Rules

**MUST:**
- Use `context.Context` as first parameter for functions that may block
- Handle all errors explicitly with proper error wrapping
- Use `errgroup` for concurrent operations with error handling
- Run `golangci-lint` before commit
- Use `defer` for cleanup operations
- Document exported functions and types

**MUST NOT:**
- Ignore errors with blank identifier (`_`)
- Use `panic` for normal error handling
- Use `init()` for complex initialization logic
- Import packages without alias when names conflict
- Use global variables for state management
- Embed credentials or secrets in code

## File Conventions

- `*_test.go` for test files
- `internal/` for private packages
- `cmd/` for main entry points
- `pkg/` for public reusable libraries
- snake_case for file names

## Testing

- Table-driven tests are preferred
- Use `testify/assert` or `go-cmp` for assertions
- Mock external dependencies with interfaces
- Use `t.Parallel()` for independent tests
