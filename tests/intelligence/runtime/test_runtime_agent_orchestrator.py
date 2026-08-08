"""
Tests for RuntimeAgentOrchestrator.
"""

from app.intelligence.runtime.runtime_agent import (
    RuntimeAgentOrchestrator,
    SimpleRuntimeAgent,
)

from app.intelligence.runtime.task import Task


def test_register_string_agent():
    orchestrator = RuntimeAgentOrchestrator()

    orchestrator.register_agent(
        "test-agent",
        capabilities=["test"],
    )

    assert orchestrator.agent_count() == 1
    assert orchestrator.has_capability("test")


def test_execute():
    orchestrator = RuntimeAgentOrchestrator()

    orchestrator.register_agent(
        SimpleRuntimeAgent(
            name="test-agent",
            capabilities=["test"],
        )
    )

    result = orchestrator.execute(
        Task(
            capability="test",
            payload={
                "value": 123
            },
        )
    )

    assert result["success"] is True
    assert result["agent"] == "test-agent"
    assert orchestrator.count() == 1


def test_scheduler_compatibility():
    orchestrator = RuntimeAgentOrchestrator()

    assert orchestrator.scheduler is orchestrator.manager


def test_clear():
    orchestrator = RuntimeAgentOrchestrator()

    orchestrator.register_agent(
        "test-agent",
        capabilities=["test"],
    )

    orchestrator.clear()

    assert orchestrator.agent_count() == 0
    assert orchestrator.count() == 0