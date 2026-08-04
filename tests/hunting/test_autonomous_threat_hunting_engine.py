from services.hunting.autonomous_threat_hunting_engine import (
    AutonomousThreatHuntingEngine
)


def test_create_hypothesis():
    engine = AutonomousThreatHuntingEngine()

    result = engine.create_hypothesis({
        "behavior": "credential_dumping",
        "risk_score": 90
    })

    assert result["priority"] == "critical"


def test_generate_hunt_query():
    engine = AutonomousThreatHuntingEngine()

    result = engine.generate_hunt_query(
        "malicious-domain.com"
    )

    assert result["status"] == "generated"


def test_detect_pattern():
    engine = AutonomousThreatHuntingEngine()

    result = engine.detect_pattern([
        {
            "event": "login anomaly",
            "severity": "critical"
        }
    ])

    assert result["matches"] == 1


def test_threat_intelligence_correlation():
    engine = AutonomousThreatHuntingEngine()

    result = engine.correlate_threat_intelligence({
        "ioc": "8.8.8.8"
    })

    assert result["matched"] is True


def test_history_tracking():
    engine = AutonomousThreatHuntingEngine()

    engine.create_hypothesis({
        "behavior": "malware_execution",
        "risk_score": 70
    })

    assert len(engine.get_hunting_history()) == 1


def test_clear_history():
    engine = AutonomousThreatHuntingEngine()

    engine.create_hypothesis({
        "behavior": "phishing",
        "risk_score": 60
    })

    result = engine.clear_history()

    assert result["status"] == "cleared"
    assert len(engine.get_hunting_history()) == 0