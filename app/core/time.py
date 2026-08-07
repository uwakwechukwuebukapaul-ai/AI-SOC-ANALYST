"""
Sentinel DNA Time Utilities

Centralized timezone-aware UTC timestamp helpers.

All application services should use these helpers instead of
datetime.utcnow() so timestamps remain timezone-aware,
consistent, and compatible with modern Python versions.
"""

from __future__ import annotations

from datetime import UTC, datetime


def utc_now() -> datetime:
    """
    Return the current timezone-aware UTC datetime.
    """
    return datetime.now(UTC)


def utc_now_iso() -> str:
    """
    Return the current timezone-aware UTC datetime as an ISO-8601 string.
    """
    return utc_now().isoformat()