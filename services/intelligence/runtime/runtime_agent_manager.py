"""
Sentinel DNA Runtime Agent Manager Compatibility Layer

Canonical implementation lives under:

    app.intelligence.runtime.runtime_agent.runtime_agent_manager

This module exists temporarily to preserve compatibility with
legacy services imports.
"""

from app.intelligence.runtime.runtime_agent.runtime_agent_manager import (
    RuntimeAgentManager,
)

__all__ = [
    "RuntimeAgentManager",
]