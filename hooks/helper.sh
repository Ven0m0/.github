#!/usr/bin/env bash
# Helper functions for hook scripts

jq_extract() {
  local path="${1}"
  local default_val="${2:-}"
  printf '%s' "${INPUT}" | jq -r "${path} // \"${default_val}\"" 2>/dev/null
}

tool_args_extract() {
  local path="${1}"
  local default_val="${2:-}"
  local fallback_path="${3:-}"
  local raw_tool_args=""

  raw_tool_args="$(jq_extract '.toolArgs // empty' '')"
  if [[ -n "${raw_tool_args}" ]] && printf '%s' "${raw_tool_args}" | jq -e . >/dev/null 2>&1; then
    printf '%s' "${raw_tool_args}" | jq -r "${path} // \"${default_val}\"" 2>/dev/null
    return
  fi

  if [[ -n "${fallback_path}" ]]; then
    jq_extract "${fallback_path}" "${default_val}"
    return
  fi

  printf '%s' "${default_val}"
}

deny_tool_use() {
  local reason="${1}"
  jq -cn --arg reason "${reason}" '{permissionDecision:"deny",permissionDecisionReason:$reason}'
  exit 0
}
