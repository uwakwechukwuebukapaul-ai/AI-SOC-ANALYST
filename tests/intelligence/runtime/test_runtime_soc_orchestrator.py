"""
Tests for the canonical SOC runtime orchestrator.
"""

from app.intelligence.runtime.runtime_soc_orchestrator import (
    RuntimeSOCOrchestrator,
)


def test_soc_runtime_initializes():
    soc = RuntimeSOCOrchestrator()

    assert soc.operations == 0
    assert soc.detection is not None
    assert soc.intelligence is not None
    assert soc.investigation is not None
    assert soc.response is not None
    assert soc.autonomous is not None


def test_soc_detection():
    soc = RuntimeSOCOrchestrator()

    result = soc.analyze_event(
        "phishing",
        {
            "sender": "attacker@example.com",
        },
    )

    assert result["success"] is True
    assert result["detected"] is False
    assert result["event_type"] == "phishing"

    assert soc.operations == 1
    assert soc.status()["detection"]["operations"] == 1


def test_soc_registered_detection():
    soc = RuntimeSOCOrchestrator()

    soc.detection.register_rule(
        "phishing",
        lambda event: {
            "detected": True,
            "severity": "high",
        },
    )

    result = soc.analyze_event(
        "phishing",
        {
            "sender": "attacker@example.com",
        },
    )

    assert result["success"] is True
    assert result["detected"] is True
    assert result["severity"] == "high"


def test_soc_clear():
    soc = RuntimeSOCOrchestrator()

    soc.analyze_event(
        "test",
        {},
    )

    soc.clear()

    assert soc.status()["operations"] == 0
    assert soc.status()["detection"]["operations"] == 0
    assert soc.status()["detection"]["detections"] == 0
    assert soc.status()["detection"]["failures"] == 0