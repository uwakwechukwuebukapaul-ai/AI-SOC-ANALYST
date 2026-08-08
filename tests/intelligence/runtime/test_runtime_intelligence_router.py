"""
Tests for RuntimeIntelligenceRouter.
"""

from app.intelligence.runtime import (
    RuntimeIntelligenceRouter,
    SimpleRuntimeAgent,
    Task,
)


def test_handler_route():
    router = RuntimeIntelligenceRouter()

    router.register(
        "test.handler",
        lambda payload: {
            "success": True,
            "payload": payload,
        },
    )

    result = router.route(
        "test.handler",
        {"value": 1},
    )

    assert result["success"] is True
    assert result["payload"]["value"] == 1


def test_agent_route():
    router = RuntimeIntelligenceRouter()

    router.register_agent(
        SimpleRuntimeAgent(
            name="test-agent",
            capabilities=["test.agent"],
        )
    )

    result = router.route(
        "test.agent",
        {
            "value": 2,
        },
    )

    assert result["success"] is True
    assert result["agent"] == "test-agent"


def test_task_route():
    router = RuntimeIntelligenceRouter()

    router.register_agent(
        SimpleRuntimeAgent(
            name="test-agent",
            capabilities=["test.task"],
        )
    )

    task = Task(
        capability="test.task",
        payload={
            "value": 3,
        },
    )

    result = router.route(task)

    assert result["success"] is True
    assert result["capability"] == "test.task"


def test_unavailable_route():
    router = RuntimeIntelligenceRouter()

    result = router.route(
        "missing.capability",
        {},
    )

    assert result is None


def test_clear():
    router = RuntimeIntelligenceRouter()

    router.register(
        "test.handler",
        lambda payload: payload,
    )

    router.clear()

    assert router.handlers == {}
    assert router.routes == 0