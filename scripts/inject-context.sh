#!/bin/bash

get_project_info() {
  if [[ -f package.json ]]; then
    jq -r '.name + " v" + .version' package.json 2>/dev/null && return
  fi

  if [[ -f pyproject.toml ]] && command -v python3 >/dev/null 2>&1; then
    python3 - <<'PY'
from pathlib import Path
import sys

try:
    import tomllib
except ModuleNotFoundError:
    print("Python 3.11 or higher is required to read pyproject.toml", file=sys.stderr)
    raise SystemExit(1)

pyproject = Path("pyproject.toml")
with pyproject.open("rb") as file:
    data = tomllib.load(file)

project = data.get("project", {})
poetry = data.get("tool", {}).get("poetry", {})
name = project.get("name") or poetry.get("name")
version = project.get("version") or poetry.get("version")

if name and version:
    print(f"{name} v{version}")
elif name:
    print(name)
else:
    print("No project name found in pyproject.toml (checked [project.name] and [tool.poetry.name])", file=sys.stderr)
    raise SystemExit(1)
PY
    return
  fi
}

PROJECT_INFO=$(get_project_info)
PROJECT_INFO=${PROJECT_INFO:-Unknown project}
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
NODE_VERSION=$(node -v 2>/dev/null || echo 'not installed')
PYTHON_VERSION=$(python3 -V 2>/dev/null || true)
PYTHON_VERSION=${PYTHON_VERSION#Python }
PYTHON_VERSION=${PYTHON_VERSION:-not installed}
ADDITIONAL_CONTEXT="Project: ${PROJECT_INFO} | Branch: ${BRANCH} | Node: ${NODE_VERSION} | Python: ${PYTHON_VERSION}"

jq -n --arg additional_context "${ADDITIONAL_CONTEXT}" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: $additional_context
  }
}'
