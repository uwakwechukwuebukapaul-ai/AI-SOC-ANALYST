"""
Tests for canonical RuntimeAgentManager.
"""

import pytest

from app.intelligence.runtime.runtime_agent import (
    RuntimeAgentManager,
    SimpleRuntimeAgent,
)

from app.intelligence.runtime.task import (
    Task,
    TaskStatus,
)


def test_register_agent():
    manager = RuntimeAgentManager()

    agent = SimpleRuntimeAgent(
        name="email-analyzer",
        capabilities=["email.analysis"],
    )

    manager.register(agent)

    assert manager.count() == 1
    assert "email-analyzer" in manager.list_agents()


def test_duplicate_agent_rejected():
    manager = RuntimeAgentManager()

    agent = SimpleRuntimeAgent(
        name="email-analyzer",
        capabilities=["email.analysis"],
    )

    manager.register(agent)

    with pytest.raises(ValueError):
        manager.register(agent)


def test_capability_lookup():
    manager = RuntimeAgentManager()

    manager.register(
        SimpleRuntimeAgent(
            name="email-analyzer",
            capabilities=["email.analysis"],
        )
    )

    assert manager.has_capability(
        "email.analysis"
    )

    assert not manager.has_capability(
        "ioc.enrichment"
    )


def test_execute_task():
    manager = RuntimeAgentManager()

    manager.register(
        SimpleRuntimeAgent(
            name="email-analyzer",
            capabilities=["email.analysis"],
        )
    )

    task = Task(
        capability="email.analysis",
        payload={
            "message": "suspicious email"
        },
    )

    result = manager.execute(task)

    assert result["success"] is True
    assert result["agent"] == "email-analyzer"
    assert result["capability"] == "email.analysis"
    assert task.status == TaskStatus.COMPLETED


def test_missing_capability_fails():
    manager = RuntimeAgentManager()

    task = Task(
        capability="missing.capability",
        payload={},
    )

    with pytest.raises(LookupError):
        manager.execute(task)

    assert task.status == TaskStatus.PENDING


def test_clear():
    manager = RuntimeAgentManager()

    manager.register(
        SimpleRuntimeAgent(
            name="test-agent",
            capabilities=["test"],
        )
    )

    manager.clear()

    assert manager.count() == 0