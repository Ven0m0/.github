"""Shared utilities for lint-and-validate scripts."""

import sys


def fix_windows_console_encoding() -> None:
    """Configure Windows console encoding for Unicode output."""
    for stream in (sys.stdout, sys.stderr):
        try:
            if hasattr(stream, "reconfigure"):
                getattr(stream, "reconfigure")(encoding="utf-8", errors="replace")
        except Exception:
            pass
