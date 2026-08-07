"""
Investigation Runtime execution layer.

Provides the orchestration boundary responsible for
executing a complete Sentinel DNA investigation.
"""

from .investigation_orchestrator import (
    InvestigationExecutionOrchestrator,
)

__all__ = [
    "InvestigationExecutionOrchestrator",
]