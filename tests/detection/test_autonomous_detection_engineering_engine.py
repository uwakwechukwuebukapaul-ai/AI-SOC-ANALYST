from services.detection.autonomous_detection_engineering_engine import (
    AutonomousDetectionEngineeringEngine
)


def test_generate_detection_rule():

    engine = AutonomousDetectionEngineeringEngine()

    result = engine.generate_detection_rule(
        "credential_dumping"
    )

    assert result["status"] == "generated"
    assert result["severity"] == "high"


def test_attack_mapping():

    engine = AutonomousDetectionEngineeringEngine()

    result = engine.map_attack_technique(
        "phishing"
    )

    assert result["technique"] == "T1566"


def test_sigma_generation():

    engine = AutonomousDetectionEngineeringEngine()

    result = engine.generate_sigma_rule(
        "ransomware"
    )

    assert result["status"] == "experimental"
    assert "detection" in result


def test_detection_quality():

    engine = AutonomousDetectionEngineeringEngine()

    rule = engine.generate_detection_rule(
        "ransomware"
    )

    result = engine.evaluate_detection_quality(
        rule
    )

    assert result["quality_score"] >= 80


def test_rule_history():

    engine = AutonomousDetectionEngineeringEngine()

    engine.generate_detection_rule(
        "phishing"
    )

    assert len(engine.get_history()) == 1


def test_clear_history():

    engine = AutonomousDetectionEngineeringEngine()

    engine.generate_detection_rule(
        "malware"
    )

    result = engine.clear_history()

    assert result["status"] == "cleared"
    assert len(engine.get_history()) == 0