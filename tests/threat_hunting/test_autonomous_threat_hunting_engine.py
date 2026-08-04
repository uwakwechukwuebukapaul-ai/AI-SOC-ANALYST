from services.threat_hunting.autonomous_threat_hunting_engine import (
    AutonomousThreatHuntingEngine
)


def test_register_indicator():
    engine = AutonomousThreatHuntingEngine()

    result = engine.register_indicator(
        "malicious-domain.com",
        "domain"
    )

    assert result["indicator"] == "malicious-domain.com"


def test_create_hunt_hypothesis():
    engine = AutonomousThreatHuntingEngine()

    result = engine.create_hunt_hypothesis(
        "Detect possible credential theft campaign"
    )

    assert result["status"] == "created"


def test_analyze_behavior():
    engine = AutonomousThreatHuntingEngine()

    result = engine.analyze_behavior(
        "Suspicious PowerShell execution detected"
    )

    assert result["risk_level"] == "high"


def test_search_ioc():
    engine = AutonomousThreatHuntingEngine()

    engine.register_indicator(
        "evil-domain.com",
        "domain"
    )

    result = engine.search_ioc("evil")

    assert result["match_count"] == 1


def test_map_attack_technique():
    engine = AutonomousThreatHuntingEngine()

    result = engine.map_attack_technique(
        "T1059 Command and Scripting Interpreter"
    )

    assert result["mapped"] is True


def test_generate_hunting_report():
    engine = AutonomousThreatHuntingEngine()

    engine.create_hunt_hypothesis(
        "Find lateral movement activity"
    )

    report = engine.generate_hunting_report()

    assert report["active_hunts"] == 1