---
applyTo: "**/*.dart,**/pubspec.yaml,**/pubspec.lock"
description: "Flutter 3.24+/Dart 3.5+: Riverpod, null safety, go_router"
---

# Flutter/Dart Standards

Version: Flutter 3.24+ / Dart 3.5+

## Toolchain

- **Build**: flutter CLI
- **Lint**: `dart analyze`, flutter_lints
- **Format**: `dart format`
- **Test**: `flutter test`
- **Packages**: pub

## Core Rules

**MUST:**
- Use Riverpod or Provider for state management
- Use `go_router` for navigation
- Use `freezed` for immutable models
- Use `const` constructors when possible
- Handle null safety properly
- Separate business logic from UI

**MUST NOT:**
- Use `setState` in complex widgets
- Use `BuildContext` across async gaps
- Ignore analyzer warnings
- Use `dynamic` type
- Block the UI thread
- Hardcode strings (use l10n)

## File Conventions

- `*_test.dart` for test files
- snake_case for file names
- PascalCase for classes
- camelCase for functions and variables
- `lib/` for source, `test/` for tests

## Testing

- Use `flutter_test` for widget tests
- Use `mockito` for mocking
- Use golden tests for UI verification
- Use `integration_test` for E2E
