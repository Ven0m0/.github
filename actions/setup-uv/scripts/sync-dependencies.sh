#!/usr/bin/env bash
set -euo pipefail

: "${FROZEN:?FROZEN is required}"

sync_args=()

if [[ "${FROZEN}" == "true" ]]; then
  sync_args+=(--frozen)
fi

case "${EXTRAS:-}" in
  "" | false | 0 | no | off)
    uv sync "${sync_args[@]}"
    ;;
  *)
    uv sync "${sync_args[@]}" --all-extras
    ;;
esac
