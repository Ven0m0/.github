#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')

if [ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]; then
  # Run linter before allowing edits
  npm run lint-staged
  npx -y biome ci --changed --no-errors-on-unmatched --skip-parse-errors --files-ignore-unknown=true --use-editorconfig=true --format-with-errors=true
  if [ $? -ne 0 ]; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Code does not pass linting"}'
  fi
fi
