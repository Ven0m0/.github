# Shell Standards

Standards for shell scripting across Bash, PowerShell, CMD, and Makefile. Each shell has unique idioms; this document covers shared principles and shell-specific best practices.

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

## Bash Standards

**File patterns**: `*.sh`, `*.bash`, `.bashrc`, `.zshrc`

### Shebang and Settings

```bash
#!/usr/bin/env bash
# shellcheck enable=all shell=bash source-path=SCRIPTDIR
set -euo pipefail; shopt -s nullglob globstar
IFS=$'\n\t' LC_ALL=C
```

**Breakdown**:
- `set -e`: Exit on error
- `set -u`: Exit on undefined variable
- `set -o pipefail`: Pipeline fails if any command fails
- `shopt -s nullglob`: Glob expansion doesn't fail if no matches
- `shopt -s globstar`: `**` matches all directories
- `IFS=$'\n\t'`: Safe word splitting (newline/tab)
- `LC_ALL=C`: Consistent locale for consistency

### Helper Functions

```bash
has() { command -v -- "$1" &>/dev/null; }
msg() { printf '%s\n' "$@"; }
log() { printf '%s\n' "$@" >&2; }
die() { printf '%s\n' "$1" >&2; exit "${2:-1}"; }

# Fast file reading (avoid cat)
fcat() { printf '%s\n' "$(<${1})"; }
```

### Conditionals and Tests

**Always use `[[ ]]` (Bash conditional compound command)**:

```bash
# GOOD: Bash conditional
if [[ -f "$file" ]]; then
    source "$file"
fi

# GOOD: Regex with =~
if [[ "$string" =~ ^[0-9]+$ ]]; then
    msg "Number detected"
fi

# BAD: POSIX test (avoid in Bash scripts)
if [ -f "$file" ]; then
    : # ...
fi
```

### Variables and Arrays

**String manipulation without external tools**:

```bash
# Substitute pattern (first match)
result="${string/find/replace}"

# Substitute pattern (all matches)
result="${string//find/replace}"

# Trim prefix
result="${string#prefix}"
result="${string##prefix}"  # Greedy

# Trim suffix
result="${string%suffix}"
result="${string%%suffix}"  # Greedy

# Default value
result="${var:-default}"
result="${var:=default}"  # Assign if empty
```

**Arrays**:

```bash
# Proper array assignment with mapfile
mapfile -t lines < "$file"

# Associative arrays
declare -A map=([key1]="value1" [key2]="value2")
for key in "${!map[@]}"; do
    echo "$key: ${map[$key]}"
done
```

### I/O and Process Substitution

**Avoid piping to loops** — use process substitution instead:

```bash
# GOOD: Process substitution preserves variable scope
while IFS= read -r line; do
    count=$((count + 1))
done < <(command | filter)
echo "Count: $count"  # Variable is accessible

# BAD: Piping loses variable scope
command | filter | while read -r line; do
    count=$((count + 1))
done
echo "Count: $count"  # count is 0 (different subshell)
```

**Here-strings for input**:

```bash
# GOOD: Here-string
while read -r item; do
    process "$item"
done <<<"$variable"

# BAD: Echo pipe (unnecessary fork)
echo "$variable" | while read -r item; do
    process "$item"
done
```

### Quoting and Expansion

**Always quote variables** unless globbing is intended:

```bash
# GOOD
rm "$file"
grep "$pattern" "$file"
echo "$count"

# BAD
rm $file          # Vulnerable to word splitting
grep $pattern     # Glob expansion unintended
[[ $count -gt 5 ]] # Can fail with unset variables
```

**Parameter expansion quoting**:

```bash
# Safe expansion
echo "${arr[@]}"          # All elements
echo "${!arr[@]}"         # All indices
echo "${var:0:5}"         # Substring
echo "${var^}"            # Uppercase first char
```

### Functions

```bash
# Function definition
validate_input() {
    local value="$1"
    local pattern="$2"

    if [[ ! "$value" =~ $pattern ]]; then
        die "Invalid input: $value" 1
    fi
}

# Usage
validate_input "$user_input" "^[a-zA-Z0-9]+$"
```

### Performance Optimization

**Minimize forks**:

```bash
# GOOD: Builtin operations
for item in "${array[@]}"; do
    [[ "$item" == *"search"* ]] && echo "$item"
done

# BAD: External grep in loop
for item in "${array[@]}"; do
    echo "$item" | grep -q "search" && echo "$item"
done
```

**Batch operations**:

```bash
# GOOD: Single find with exec
find . -type f -name "*.log" -exec rm {} \;

# Process multiple files at once
while IFS= read -r -d '' file; do
    process "$file"
done < <(find . -type f -print0)
```

**Precompile patterns**:

```bash
# GOOD: Compile once
pattern="^[0-9]{3}-[0-9]{4}$"
for item in "${items[@]}"; do
    [[ "$item" =~ $pattern ]] && echo "Valid"
done
```

### Linting and Formatting

```bash
# Check script
shellcheck script.sh

# Harden script (security analysis)
shellharden script.sh --replace

# Format script (2-space indent)
shfmt -i 2 -bn -ci -s -w script.sh
```

### Forbidden Patterns

- ❌ `eval` — code injection risk
- ❌ Backticks (`` ` ``) — use `$()` instead
- ❌ Parsing `ls` output — use globbing instead
- ❌ Unquoted variables — always quote
- ❌ `expr` — use `$(())` arithmetic
- ❌ Sourcing remote files

---

## PowerShell Standards

**File patterns**: `*.ps1`, `*.psm1` (module), `*.psd1` (manifest)

### Script Metadata

```powershell
<#
.SYNOPSIS
    Brief description of what the script does

.DESCRIPTION
    Detailed description with more context

.PARAMETER Path
    Path to the resource to process

.EXAMPLE
    .\script.ps1 -Path "C:\data"

.NOTES
    Author: John Doe
    Last Modified: 2024-02-01
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Path,

    [Parameter(Mandatory=$false)]
    [int]$Timeout = 30
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
```

### Cmdlet Naming and Style

```powershell
# GOOD: Verb-Noun naming (PowerShell approved verbs)
function Get-UserById {
    param(
        [Parameter(Mandatory=$true)]
        [string]$UserId
    )

    # Implementation
}

# Use approved verbs: Get, Set, New, Remove, Test, Start, Stop, Invoke, Confirm, etc.
# Full list: Get-Verb
```

### Error Handling

```powershell
# Try-catch-finally pattern
try {
    $result = Get-Item $Path -ErrorAction Stop
    Write-Host "Found: $result"
}
catch [ItemNotFoundException] {
    Write-Error "Item not found: $Path"
    exit 1
}
catch {
    Write-Error "Unexpected error: $_"
    exit 2
}
finally {
    # Cleanup
}
```

### Pipeline and Objects

```powershell
# GOOD: Working with objects through the pipeline
Get-Process |
    Where-Object {$_.WorkingSet -gt 100MB} |
    ForEach-Object {
        [PSCustomObject]@{
            Name = $_.Name
            Memory = "$([math]::Round($_.WorkingSet/1MB)) MB"
        }
    }

# Avoid string manipulation; use objects
$obj = [PSCustomObject]@{
    Name = "John"
    Age = 30
    Email = "john@example.com"
}
$obj | Export-Csv "users.csv"
```

### Modules and Functions

```powershell
# Export public functions in module manifest
Export-ModuleMember -Function Get-User, New-User

# Use filters for pipeline
filter Where-Large {
    if ($_.Size -gt 10MB) {
        $_
    }
}

Get-ChildItem | Where-Large
```

### Forbidden Patterns

- ❌ Hardcoded credentials — use SecureString or credential objects
- ❌ `Invoke-Expression` with untrusted input — code injection risk
- ❌ `ConvertFrom-Json` with `-Depth 1` — insufficient for complex objects
- ❌ Unquoted paths with spaces — always quote
- ❌ Ignoring errors with `$ErrorActionPreference = "SilentlyContinue"`

---

## CMD/Batch Standards

**File patterns**: `*.bat`, `*.cmd`

### Script Header

```batch
@echo off
setlocal enabledelayedexpansion
setlocal enableextensions
```

**Breakdown**:
- `@echo off`: Don't echo command being executed
- `setlocal enabledelayedexpansion`: Use `!var!` for delayed expansion
- `setlocal enableextensions`: Enable command extensions (safer, more features)

### Variables and Expansion

```batch
:: Immediate expansion (normal)
set "name=John"
echo %name%

:: Delayed expansion (in code blocks)
setlocal enabledelayedexpansion
if exist "file.txt" (
    set "count=1"
    echo Count: !count!     :: Use !var! not %var% in code blocks
)
```

### Control Flow

```batch
:: If statements
if exist "file.txt" (
    echo File exists
) else (
    echo File not found
)

:: If with conditions
if "%errorlevel%"=="0" (
    echo Success
) else (
    echo Failed with code %errorlevel%
)

:: For loops
for %%i in (1 2 3) do (
    echo Item: %%i
)

:: For directories
for /d %%i in (C:\*) do (
    echo Directory: %%i
)
```

### Functions/Subroutines

```batch
:: Call a subroutine with parameters
call :process_file "input.txt"

:: Function definition
:process_file
set "filename=%~1"
set "fullpath=%~f1"     :: Full path
set "drive=%~d1"        :: Drive letter
set "path=%~p1"         :: Directory path
set "filename=%~n1"     :: Filename without extension
set "extension=%~x1"    :: File extension

echo Processing: %fullpath%
exit /b 0               :: Return from function

:error_handler
echo Error: %errorlevel%
exit /b 1
```

### Error Handling

```batch
:: Check previous command's exit code
if errorlevel 1 (
    echo Error occurred
    goto :error_handler
)

:: Or use conditional execution
command && echo Success || echo Failure
```

### Forbidden Patterns

- ❌ Unquoted paths with spaces: always use `"%path%"`
- ❌ Using `%var%` inside code blocks with delayed expansion needed
- ❌ No error checking — always verify errorlevel
- ❌ Modifying environment variables without `setlocal`

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

