from services.detection.autonomous_detection_engineering_engine import (
    AutonomousDetectionEngineeringEngine,
)


def test_register_detection_rule():
    engine = AutonomousDetectionEngineeringEngine()

    result = engine.register_detection_rule(
        "DET-001",
        "Suspicious PowerShell Execution",
        "high",
        "T1059.001",
    )

    assert result["rule_id"] == "DET-001"
    assert result["status"] == "active"


def test_analyze_detection_rule():
    engine = AutonomousDetectionEngineeringEngine()

    engine.register_detection_rule(
        "DET-001",
        "Malware Execution",
        "critical",
        "T1204",
    )

    result = engine.analyze_detection_rule("DET-001")

    assert result["quality_score"] == 90
    assert result["coverage"] == "high"


def test_detection_gap_analysis():
    engine = AutonomousDetectionEngineeringEngine()

    result = engine.identify_detection_gap(
        "enterprise_network"
    )

    assert result["priority"] == "high"
    assert "credential_access" in result["missing_coverage"]


def test_optimize_detection_rule():
    engine = AutonomousDetectionEngineeringEngine()

    result = engine.optimize_detection_rule(
        "DET-001"
    )

    assert result["confidence"] > 0.9
    assert "reduce false positives" in result["improvements"]


def test_generate_detection_strategy():
    engine = AutonomousDetectionEngineeringEngine()

    result = engine.generate_detection_strategy(
        "ransomware"
    )

    assert result["threat_type"] == "ransomware"
    assert result["confidence"] > 0.9


def test_detection_history():
    engine = AutonomousDetectionEngineeringEngine()

    engine.register_detection_rule(
        "DET-001",
        "Test Rule",
        "medium",
        "T1059",
    )

    history = engine.get_history()

    assert len(history) == 1
    assert history[0]["action"] == "register_rule"