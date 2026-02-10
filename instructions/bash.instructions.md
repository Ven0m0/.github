---
description: 'Bash and shell scripting standards with best practices for safety, performance, and maintainability'
applyTo: '**/*.sh, **/*.bash'
---

# Bash Scripting Standards

Standards for Bash scripting with focus on safety, reliability, and performance. Includes POSIX-compatible patterns and modern Bash idioms.

## Shared Shell Principles

<Goals>
  
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
<Goals>

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

### Testing

```bash
# Bash unit testing
bats tests/*.bats          # Bash Automated Testing System
```

### Forbidden Patterns

- ❌ `eval` — code injection risk
- ❌ Backticks (`` ` ``) — use `$()` instead
- ❌ Parsing `ls` output — use globbing instead
- ❌ Unquoted variables — always quote
- ❌ `expr` — use `$(())` arithmetic
- ❌ Sourcing remote files

---

## Exit Codes

```bash
exit 0      # Success
exit 1      # General error
exit 127    # Command not found
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
