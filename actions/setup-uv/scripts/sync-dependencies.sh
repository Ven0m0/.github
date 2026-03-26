#!/usr/bin/env bash
set -euo pipefail

sync_args=()

if [[ "${FROZEN:-true}" == "true" ]]; then
  sync_args+=(--frozen)
fi

if [[ -n "${EXTRAS:-}" ]]; then
  uv sync "${sync_args[@]}" --all-extras
else
  uv sync "${sync_args[@]}"
fi
