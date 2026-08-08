"""
Tests for the canonical runtime detection orchestrator.
"""

from app.intelligence.runtime.runtime_detection_orchestrator import (
    RuntimeDetectionOrchestrator,
)


def test_detection_init():
    detection = RuntimeDetectionOrchestrator()

    assert detection.operations == 0
    assert detection.detections == 0
    assert detection.failures == 0
    assert detection.rules == {}


def test_register_rule():
    detection = RuntimeDetectionOrchestrator()

    detection.register_rule(
        "phishing",
        lambda event: {
            "detected": True,
            "reason": "phishing activity",
        },
    )

    assert detection.has_rule("phishing")
    assert "phishing" in detection.status()["rules"]


def test_evaluate_registered_rule():
    detection = RuntimeDetectionOrchestrator()

    detection.register_rule(
        "phishing",
        lambda event: {
            "detected": True,
            "reason": "suspicious sender",
        },
    )

    result = detection.evaluate(
        "phishing",
        {
            "sender": "attacker@example.com",
        },
    )

    assert result["success"] is True
    assert result["detected"] is True
    assert result["event_type"] == "phishing"
    assert result["rule"] == "phishing"
    assert result["reason"] == "suspicious sender"

    assert detection.operations == 1
    assert detection.detections == 1


def test_evaluate_without_rule():
    detection = RuntimeDetectionOrchestrator()

    result = detection.evaluate(
        "phishing",
        {
            "sender": "attacker@example.com",
        },
    )

    assert result["success"] is True
    assert result["detected"] is False
    assert result["event_type"] == "phishing"
    assert detection.operations == 1


def test_detection_rule_boolean_result():
    detection = RuntimeDetectionOrchestrator()

    detection.register_rule(
        "malware",
        lambda event: True,
    )

    result = detection.evaluate(
        "malware",
        {},
    )

    assert result["success"] is True
    assert result["detected"] is True


def test_detection_rule_failure():
    detection = RuntimeDetectionOrchestrator()

    def failing_rule(event):
        raise RuntimeError("rule failure")

    detection.register_rule(
        "broken",
        failing_rule,
    )

    result = detection.evaluate(
        "broken",
        {},
    )

    assert result["success"] is False
    assert result["detected"] is False
    assert "rule failure" in result["error"]
    assert detection.failures == 1


def test_detection_clear():
    detection = RuntimeDetectionOrchestrator()

    detection.register_rule(
        "test",
        lambda event: {
            "detected": True,
        },
    )

    detection.evaluate(
        "test",
        {},
    )

    detection.clear()

    assert detection.operations == 0
    assert detection.detections == 0
    assert detection.failures == 0
    assert detection.rules == {}


def test_detection_status():
    detection = RuntimeDetectionOrchestrator()

    detection.register_rule(
        "test",
        lambda event: {
            "detected": True,
        },
    )

    detection.evaluate(
        "test",
        {},
    )

    status = detection.status()

    assert status["operations"] == 1
    assert status["detections"] == 1
    assert status["failures"] == 0
    assert status["count"] == 1
    assert status["rules"] == ["test"]