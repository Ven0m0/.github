#!/usr/bin/env bash
set -euo pipefail

UV_VERSION=$(uv --version | cut -d' ' -f2)
echo "version=${UV_VERSION}" >> "${GITHUB_OUTPUT}"
echo "Using uv ${UV_VERSION}"
