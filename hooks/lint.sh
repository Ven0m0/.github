#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.toolName')

if [ "$TOOL_NAME" = "edit" ] || [ "$TOOL_NAME" = "create" ]; then
  # Run linter before allowing edits
  bun run lint-staged
  bunx biome ci --changed --no-errors-on-unmatched --skip-parse-errors --files-ignore-unknown=true --use-editorconfig=true --format-with-errors=true
  uvx ruff format
  if [ $? -ne 0 ]; then
    echo '{"permissionDecision":"deny","permissionDecisionReason":"Code does not pass linting"}'
  fi
fi
