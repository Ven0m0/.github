---
description: 'Bash scripting standards: safety, performance, and modern idioms'
applyTo: '**/*.sh,**/*.bash'
---

# Bash Scripting Standards

<Goals>

- Fail fast: `set -euo pipefail`, strict error handling
- Performance: minimize forks, use builtins, batch operations
- Portability: POSIX where possible, document OS requirements
- Clarity: descriptive names, explain non-obvious logic

</Goals>

## Tooling Preferences

| Task | Preferred | Fallback |
|------|-----------|----------|
| Search | `rg` | `grep` |
| Find files | `fd` | `find` |
| JSON | `jq` | - |
| Edit | `sd` | `sed` |
| List | `eza` | `ls` |
| View | `bat` | `cat` |
| Download | `aria2c` | `curl` |

## Template

```bash
#!/usr/bin/env bash
# shellcheck enable=all shell=bash source-path=SCRIPTDIR
set -euo pipefail; shopt -s nullglob globstar
IFS=$'\n\t' LC_ALL=C

has(){ command -v -- "$1" &>/dev/null; }
msg(){ printf '%s\n' "$@"; }
log(){ printf '%s\n' "$@" >&2; }
die(){ printf '%s\n' "$1" >&2; exit "${2:-1}"; }
fcat(){ printf '%s\n' "$(<${1})"; }
```

<Standards>

**Conditionals**: Always `[[ ]]`, regex with `=~`
**Arrays**: `mapfile -t`, `declare -A` for associative
**Strings**: `${v//p/r}` substitute, `${v%%p*}` trim - no sed for simple edits
**I/O**: `<<<"$v"` here-string, `< <(cmd)` process substitution (preserves scope)
**Variables**: Always quote (`"$var"`), `${var:-default}` for defaults
**Functions**: `local` for variables, validate inputs, return codes

</Standards>

## Key Patterns

```bash
# Process substitution preserves variable scope
while IFS= read -r line; do
    count=$((count + 1))
done < <(command | filter)

# Array from file
mapfile -t lines < "$file"

# Precompile patterns
pattern="^[0-9]{3}-[0-9]{4}$"
for item in "${items[@]}"; do
    [[ "$item" =~ $pattern ]] && echo "Valid"
done
```

## Linting

```bash
shellcheck script.sh
shellharden script.sh --replace
shfmt -i 2 -bn -ci -s -w script.sh
```

<Limitations>

- No `eval` (code injection risk)
- No backticks (use `$()`)
- No `ls` parsing (use globbing)
- No unquoted variables
- No `expr` (use `$(())`)
- No sourcing remote files

</Limitations>

<Security>

- No hardcoded credentials
- Input validation before use
- Error messages must not leak paths or sensitive data
- No dynamic code execution from untrusted sources
- Temporary files via `mktemp`, cleaned up in trap

</Security>
