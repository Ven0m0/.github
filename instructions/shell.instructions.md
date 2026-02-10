---
description: 'General shell scripting best practices for bash, sh, zsh'
applyTo: '**/*.sh'
---

# Shell Scripting Guidelines

For detailed Bash standards, see `bash.instructions.md`.

<Goals>

- Clean, simple, concise scripts for automation and testing
- Safe expansions: double-quote variables, avoid `eval`
- Modern Bash features when portability allows; POSIX fallback when needed
- Reliable parsers (`jq`/`yq`) for structured data over ad-hoc text processing

</Goals>

<Standards>

**Safety**: `set -euo pipefail`, validate parameters, `trap` for cleanup, `readonly` for constants, `mktemp` for temp files
**Structure**: Shebang (`#!/bin/bash`), header comment, defaults at top, functions for reuse
**JSON/YAML**: Use `jq`/`yq`, quote filters, `--raw-output` for strings, fail fast on parser errors

</Standards>

```bash
#!/bin/bash
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0")"
TEMP_DIR=""

cleanup(){ [[ -n "${TEMP_DIR:-}" && -d "$TEMP_DIR" ]] && rm -rf "$TEMP_DIR"; }
trap cleanup EXIT

validate_requirements(){
    [[ -z "$RESOURCE_GROUP" ]] && { echo "Error: Resource group required" >&2; exit 1; }
}

main(){
    validate_requirements
    TEMP_DIR="$(mktemp -d)"
    # Main logic
}
main "$@"
```

<Limitations>

- No `eval` or dynamic code execution
- No parsing `ls` output
- No unquoted variable expansions
- No hardcoded credentials

</Limitations>
