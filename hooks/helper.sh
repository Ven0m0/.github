#!/usr/bin/env bash
# Helper functions for hook scripts

# Extracts a value from the INPUT variable using jq
# $1: The jq path to extract
# $2: (Optional) A default value to fall back to if jq extraction fails
jq_extract() {
  local path="$1"
  local default_val="${2:-}"
  printf '%s' "$INPUT" | jq -r "$path // \"$default_val\"" 2>/dev/null
}
