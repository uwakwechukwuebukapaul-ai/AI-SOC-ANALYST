"""
Tests for RuntimeInvestigationOrchestrator.
"""

from app.intelligence.runtime import (
    RuntimeInvestigationOrchestrator,
    SimpleRuntimeAgent,
)


def test_investigation():
    orchestrator = RuntimeInvestigationOrchestrator()

    orchestrator.register_agent(
        SimpleRuntimeAgent(
            name="investigator",
            capabilities=["investigate.alert"],
        )
    )

    result = orchestrator.investigate(
        "investigate.alert",
        {
            "alert_id": "ALERT-001",
        },
    )

    assert result["success"] is True
    assert result["agent"] == "investigator"
    assert orchestrator.count() == 1


def test_clear():
    orchestrator = RuntimeInvestigationOrchestrator()

    orchestrator.register_agent(
        SimpleRuntimeAgent(
            name="investigator",
            capabilities=["investigate.alert"],
        )
    )

    orchestrator.investigate(
        "investigate.alert",
        {},
    )

    orchestrator.clear()

    assert orchestrator.count() == 0
    assert orchestrator.router.orchestrator.agent_count() == 0