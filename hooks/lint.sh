#!/usr/bin/env bash
set -euo pipefail

INPUT="$(cat 2>/dev/null)"

# Source helper script
source "$(dirname "$0")/helper.sh"
TOOL_NAME="$(jq_extract '.toolName // .tool_name' '')"
TOOL_NAME_LC="${TOOL_NAME,,}"
FILE_PATH="$(tool_args_extract '.path // .file_path // empty' '' '.tool_input.file_path')"

if [[ "${TOOL_NAME_LC}" =~ ^(create|edit|strreplace|write)$ ]] && [[ -n "${FILE_PATH}" ]] && [[ -f "${FILE_PATH}" ]] && command -v biome >/dev/null 2>&1; then
  biome check --no-errors-on-unmatched --files-ignore-unknown=true --use-editorconfig=true "${FILE_PATH}" >/dev/null 2>&1 || true
fi
exit 0
