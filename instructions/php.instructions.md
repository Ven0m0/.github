---
applyTo: "**/*.php,**/composer.json,**/composer.lock"
description: "PHP 8.3+: strict types, PHPStan level 9, typed properties"
---

# PHP Standards

Version: PHP 8.3+

## Toolchain

- **Packages**: Composer
- **Lint**: PHP_CodeSniffer, PHPStan level 9
- **Format**: PHP-CS-Fixer
- **Test**: PHPUnit >= 85% coverage

## Core Rules

**MUST:**
- Use strict types (`declare(strict_types=1)`)
- Use typed properties and return types
- Use constructor property promotion
- Use named arguments for clarity
- Use readonly properties for immutability
- Handle exceptions with proper types

**MUST NOT:**
- Use `@` error suppression operator
- Use global variables
- Mix HTML and PHP logic directly
- Use deprecated functions
- Ignore PHPStan errors
- Store credentials in code

## File Conventions

- `*Test.php` for test files
- PSR-4 autoloading structure
- PascalCase for classes
- camelCase for methods
- One class per file

## Testing

- Use PHPUnit with data providers
- Use Mockery or PHPUnit mocks
- Use Pest for expressive tests
- Use database transactions for isolation
