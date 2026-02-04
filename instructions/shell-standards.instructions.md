---
description: 'Makefile standards and cross-shell patterns for consistent build automation and task management'
applyTo: '**/Makefile, **/*.mk, **/*.make'
---

# Makefile and Cross-Shell Standards

Standards for Makefiles and cross-shell patterns. For shell-specific standards, see:
- `bash.instructions.md` - Bash scripting standards
- `powershell.instructions.md` - PowerShell scripting standards
- `cmd.instructions.md` - CMD/Batch scripting standards

## Shared Principles

### Safety and Reliability

1. **Fail Fast**: Detect errors immediately and exit
   - All scripts: Use strict error handling
   - No silent failures or ignored errors
   - Explicit validation before operations

2. **Performance**: Minimize forks and I/O
   - Batch operations together
   - Use built-in commands over external tools
   - Cache computed values

3. **Portability**: Code should run across platforms
   - Use POSIX-compatible syntax where possible
   - Avoid shell-specific features when unnecessary
   - Document OS requirements

4. **Clarity**: Scripts should be readable and maintainable
   - Descriptive variable and function names
   - Comments explaining non-obvious logic
   - Consistent style and formatting

### Tooling Preferences

Modern tools prioritized with legacy fallbacks:

| Task | Preferred | Fallback |
|------|-----------|----------|
| Search files | `rg` (ripgrep) | `grep` |
| Find files | `fd` | `find` |
| Streaming | `jq` | Legacy tools |
| Format/edit | `sd` | `sed` |
| List files | `eza` | `ls` |
| View files | `bat` | `cat` |
| Download | `aria2c` | `curl` |


---

## Makefile Standards

**File patterns**: `Makefile`, `makefile`, `*.make`

### Basic Structure

```makefile
# Variables
SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := help

# Phony targets (not files)
.PHONY: help build test clean deploy

# Help target
help:
    @grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
        awk 'BEGIN {FS = ":.*?## "} {printf "%-20s %s\n", $$1, $$2}'
```

### Target Definition

```makefile
# Simple target
build: ## Build the project
    @echo "Building..."
    $(MAKE) -C src/

# Target with dependencies
test: build ## Run tests
    @echo "Testing..."
    pytest tests/

# Target with variables
deploy: test ## Deploy to production
    @echo "Deploying to $(DEPLOY_ENV)"
    ./scripts/deploy.sh
```

### Variables and Expansion

```makefile
# Simple variable assignment
VERSION := 1.0.0
BUILD_DIR := build

# Automatic variables
# $@: Target name
# $<: First prerequisite
# $^: All prerequisites
# $*: Stem of file in pattern rule

compile: src/main.o src/util.o
    gcc -o $@ $^

src/%.o: src/%.c
    gcc -c $< -o $@
```

### Functions

```makefile
# String functions
SOURCES := $(wildcard src/*.c)                  # Find all .c files
OBJECTS := $(SOURCES:.c=.o)                    # Replace .c with .o
UPPER := $(shell echo "$(name)" | tr a-z A-Z)  # External command

# Conditional
ifeq ($(OS),Linux)
    LDFLAGS := -lm
else
    LDFLAGS :=
endif
```

### Best Practices

```makefile
# Use tabs, not spaces (required by Make)
clean: ## Remove build artifacts
    rm -rf build/
    rm -f *.o

# Use @ to suppress echoing the command
verbose:
    @echo "This won't show the echo command"
    echo "This will show the echo command"

# Use + for commands that should run despite errors
force:
    +rm -rf build/

# Silent mode
.SILENT:
    quiet: echo "No echoing"
```

### Forbidden Patterns

- ❌ Using spaces instead of tabs in recipes — will cause parsing errors
- ❌ Assuming commands exist without checking — use `command -v` or `which`
- ❌ Not using .PHONY for non-file targets — causes confusion
- ❌ Complex logic in Makefile — use shell scripts instead

---

## Cross-Shell Patterns

### Exit Codes

```bash
# Bash
exit 0      # Success
exit 1      # General error
exit 127    # Command not found
```

```powershell
# PowerShell
exit 0      # Success
exit 1      # General error
exit 127    # Command not found
```

### Input Validation

All shells: Validate inputs early, fail with clear error messages, use strict mode.

### Logging and Output

- Use `msg()` / `Write-Host` for user messages
- Use `log()` / `Write-Error` for error messages
- Be specific in error messages with context

---

## Tooling and Quality

### Linting and Analysis

```bash
# Bash
shellcheck script.sh                  # Linting
shellharden script.sh --replace       # Security hardening
shfmt -i 2 -w script.sh              # Formatting

# PowerShell
Invoke-ScriptAnalyzer -Path script.ps1
```

### Testing

```bash
# Bash unit testing
bats tests/*.bats          # Bash Automated Testing System

# PowerShell Pester
Invoke-Pester -Path tests/
```

---

## Security Checklist

- [ ] No hardcoded credentials
- [ ] Input validation before use
- [ ] Error messages don't leak paths or sensitive data
- [ ] No dynamic code execution from untrusted sources
- [ ] Proper quoting for variables and expansions
- [ ] Exit codes checked appropriately
- [ ] Temporary files created securely

