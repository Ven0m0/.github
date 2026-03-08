#!/usr/bin/env bash
set -o pipefail

INPUT=$(cat 2>/dev/null)
TOOL_NAME=$(printf '%s' "$INPUT" | jq -r '.tool_name // .toolName // ""' 2>/dev/null)

if [[ "$TOOL_NAME" = "edit" || "$TOOL_NAME" = "create" ]]; then
  npm run lint-staged
  if ! npx -y biome ci --changed --no-errors-on-unmatched --skip-parse-errors \
    --files-ignore-unknown=true --use-editorconfig=true --format-with-errors=true; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Code does not pass linting"}'
  fi
fi
exit 0
