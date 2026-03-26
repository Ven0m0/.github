#!/usr/bin/env bash
set -euo pipefail

uv python install "${PYTHON_VERSION}"
INSTALLED_VERSION=$(uv run python --version | cut -d' ' -f2)
echo "version=${INSTALLED_VERSION}" >> "${GITHUB_OUTPUT}"
echo "Installed Python ${INSTALLED_VERSION}"
