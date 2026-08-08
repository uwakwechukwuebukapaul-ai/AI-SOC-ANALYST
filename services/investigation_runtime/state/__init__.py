"""
Investigation runtime state management.

Provides the public state model and manager used to track
investigation lifecycle independently from persistence.
"""

from .investigation_state import (
    InvestigationState,
    InvestigationStatus,
)
from .state_manager import (
    InvestigationStateManager,
)

__all__ = [
    "InvestigationState",
    "InvestigationStatus",
    "InvestigationStateManager",
]