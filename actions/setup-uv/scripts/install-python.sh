#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_OUTPUT:?GITHUB_OUTPUT is required}"

uv python install "${PYTHON_VERSION}"
INSTALLED_VERSION=$(uv run python --version | cut -d' ' -f2)
echo "version=${INSTALLED_VERSION}" >> "${GITHUB_OUTPUT}"
echo "Installed Python ${INSTALLED_VERSION}"
