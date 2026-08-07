"""
Investigation workflow state machine.
"""

from __future__ import annotations

from enum import Enum


class WorkflowState(str, Enum):
    CREATED = "created"
    ANALYZING = "analyzing"
    ENRICHING = "enriching"
    DECIDING = "deciding"
    RESPONDING = "responding"
    COMPLETED = "completed"
    FAILED = "failed"