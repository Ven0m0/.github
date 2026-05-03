"""Shared utilities for lint-and-validate scripts."""

import sys


def fix_windows_console_encoding() -> None:
    """Configure Windows console encoding for Unicode output."""
    if hasattr(sys.stdout, "reconfigure"):
        getattr(sys.stdout, "reconfigure")(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        getattr(sys.stderr, "reconfigure")(encoding="utf-8", errors="replace")
