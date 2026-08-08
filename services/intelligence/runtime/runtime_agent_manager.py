"""
Sentinel DNA Runtime Agent Manager Compatibility Layer

The canonical implementation lives under:

    app.intelligence.runtime.runtime_agent.runtime_agent_manager

This module exists to preserve compatibility with legacy services imports
while Sentinel DNA transitions to the canonical application runtime layer.
"""

from app.intelligence.runtime.runtime_agent.runtime_agent_manager import (
    RuntimeAgentManager,
)

__all__ = [
    "RuntimeAgentManager",
]