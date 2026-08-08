"""
Sentinel DNA Runtime Agent Orchestrator Compatibility Layer

Canonical implementation lives under:

    app.intelligence.runtime.runtime_agent.runtime_agent_orchestrator

This module exists temporarily to preserve compatibility with
legacy services imports.
"""

from app.intelligence.runtime.runtime_agent.runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
    SimpleRuntimeAgent,
)

__all__ = [
    "RuntimeAgentOrchestrator",
    "SimpleRuntimeAgent",
]