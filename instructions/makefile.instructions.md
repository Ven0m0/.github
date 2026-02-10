---
description: 'Makefile standards and cross-shell patterns for build automation'
applyTo: '**/Makefile,**/*.mk,**/*.make'
---

# Makefile and Cross-Shell Standards

For shell-specific standards, see: `bash.instructions.md`, `powershell.instructions.md`, `cmd.instructions.md`

<Goals>

- Fail fast: detect errors immediately
- Performance: minimize forks, batch operations
- Clarity: descriptive targets, help documentation

</Goals>

## Makefile Standards

```makefile
SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := help
.PHONY: help build test clean deploy

help:
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "} {printf "%-20s %s\n", $$1, $$2}'

build: ## Build the project
	@echo "Building..."
	$(MAKE) -C src/

test: build ## Run tests
	pytest tests/
```

<Standards>

**Variables**: `:=` for simple assignment. Automatic: `$@` (target), `$<` (first prereq), `$^` (all prereqs), `$*` (stem)
**Targets**: `.PHONY` for non-file targets. `##` comment after target for help docs
**Recipes**: Tabs required (not spaces). `@` suppresses echo. `+` for force-run
**Conditionals**: `ifeq`/`ifneq` for platform-specific logic

</Standards>

<Limitations>

- No spaces instead of tabs in recipes
- No assuming commands exist without checking
- No missing `.PHONY` for non-file targets
- No complex logic in Makefile (use shell scripts)

</Limitations>

## Cross-Shell Patterns

**Exit Codes**: `0` success, `1` general error, `127` command not found
**Input Validation**: Validate early, fail with clear messages, use strict mode
**Logging**: User messages to stdout, errors to stderr, include context

<Security>

- No hardcoded credentials
- Input validation before use
- Error messages must not leak sensitive data
- Proper quoting for variables
- Temporary files created securely

</Security>
