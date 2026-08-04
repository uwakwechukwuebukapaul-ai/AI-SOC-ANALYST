from services.detection.autonomous_detection_engine import (
    AutonomousDetectionEngine
)


def test_create_detection_rule():
    engine = AutonomousDetectionEngine()

    rule = engine.create_detection_rule(
        "PowerShell Abuse",
        "powershell",
        "high"
    )

    assert rule["name"] == "PowerShell Abuse"
    assert len(engine.rules) == 1


def test_analyze_suspicious_behavior():
    engine = AutonomousDetectionEngine()

    result = engine.analyze_behavior(
        {
            "suspicious_command": True,
            "unknown_process": True
        }
    )

    assert result["detected"] is True
    assert result["risk_score"] == 70


def test_low_risk_behavior():
    engine = AutonomousDetectionEngine()

    result = engine.analyze_behavior({})

    assert result["detected"] is False
    assert result["risk_score"] == 0


def test_rule_matching():
    engine = AutonomousDetectionEngine()

    rule = engine.create_detection_rule(
        "Malicious Script",
        "python",
        "medium"
    )

    result = engine.evaluate_rule(
        rule,
        {
            "command": "python malware.py"
        }
    )

    assert result["matched"] is True


def test_detection_optimization():
    engine = AutonomousDetectionEngine()

    result = engine.optimize_detection(
        "Reduce false positives"
    )

    assert result["action"] == "Detection rule optimization applied"


def test_detection_history():
    engine = AutonomousDetectionEngine()

    history = engine.get_detection_history()

    assert "detections" in history
    assert "optimizations" in history
    assert "rules" in history