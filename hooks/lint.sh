#!/bin/bash
INPUT=$(cat 2>/dev/null)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName' 2>/dev/null)

if [[ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]]; then
  # Run linter before allowing edits
  npm run lint-staged
  npx -y biome ci --changed --no-errors-on-unmatched --skip-parse-errors --files-ignore-unknown=true --use-editorconfig=true --format-with-errors=true
  #uvx ruff format
  if [[ $? -ne 0 ]]; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Code does not pass linting"}'
  fi
fi
exit 0
