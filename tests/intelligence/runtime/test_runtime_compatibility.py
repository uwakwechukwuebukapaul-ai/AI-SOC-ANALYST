"""
Tests for runtime compatibility imports.
"""

from app.intelligence.runtime.runtime_agent import (
    RuntimeAgentManager,
    RuntimeAgentOrchestrator,
    SimpleRuntimeAgent,
)

from services.intelligence.runtime.runtime_agent_manager import (
    RuntimeAgentManager as LegacyManager,
)

from services.intelligence.runtime.runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator as LegacyOrchestrator,
    SimpleRuntimeAgent as LegacyAgent,
)


def test_canonical_imports():
    assert RuntimeAgentManager is not None
    assert RuntimeAgentOrchestrator is not None
    assert SimpleRuntimeAgent is not None


def test_legacy_manager_points_to_canonical():
    assert LegacyManager is RuntimeAgentManager


def test_legacy_orchestrator_points_to_canonical():
    assert LegacyOrchestrator is RuntimeAgentOrchestrator
    assert LegacyAgent is SimpleRuntimeAgent