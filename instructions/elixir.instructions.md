---
applyTo: "**/*.ex,**/*.exs,**/mix.exs"
description: "Elixir 1.17+: pattern matching, OTP, fault tolerance"
---

# Elixir Standards

Version: Elixir 1.17+

## Toolchain

- **Build**: Mix
- **Lint**: Credo
- **Format**: `mix format`
- **Test**: ExUnit
- **Types**: Dialyzer

## Core Rules

**MUST:**
- Use pattern matching for control flow
- Use `with` for chained operations
- Use GenServer for stateful processes
- Use Supervisor trees for fault tolerance
- Write `@spec` for public functions
- Use `@moduledoc` and `@doc` for documentation

**MUST NOT:**
- Use `try/catch` for control flow
- Spawn processes without supervision
- Use mutable state (Agent misuse)
- Ignore dialyzer warnings
- Use string concatenation in loops
- Leave `IO.inspect` debug calls in production

## File Conventions

- `*_test.exs` for test files
- snake_case for modules and functions
- PascalCase for module names
- `lib/` for application code
- `test/` for test files

## Testing

- Use ExUnit with `setup` blocks
- Use Mox for mocking behaviors
- Use `async: true` for isolated tests
- Use ExMachina for test factories
