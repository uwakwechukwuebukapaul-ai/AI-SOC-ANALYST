"""
Sentinel DNA Investigation State

Tracks investigation lifecycle.
"""

from enum import Enum


class InvestigationState(str, Enum):
    """
    Investigation lifecycle states.
    """

    CREATED = "created"

    RUNNING = "running"

    ANALYZING = "analyzing"

    COMPLETED = "completed"

    FAILED = "failed"

    CLOSED = "closed"