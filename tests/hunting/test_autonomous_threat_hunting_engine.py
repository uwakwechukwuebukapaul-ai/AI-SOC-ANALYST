from services.hunting.autonomous_threat_hunting_engine import (
    AutonomousThreatHuntingEngine
)


def test_create_hunting_hypothesis():
    engine = AutonomousThreatHuntingEngine()

    result = engine.create_hunting_hypothesis(
        "Credential Theft Investigation",
        "Search for credential dumping behavior",
        "T1003"
    )

    assert result["technique"] == "T1003"
    assert len(engine.hunts) == 1


def test_generate_query():
    engine = AutonomousThreatHuntingEngine()

    hypothesis = {
        "technique": "T1059"
    }

    result = engine.generate_query(hypothesis)

    assert "T1059" in result["query"]


def test_detect_threat_activity():
    engine = AutonomousThreatHuntingEngine()

    result = engine.analyze_hunting_result(
        {
            "suspicious_process": True,
            "credential_activity": True
        }
    )

    assert result["threat_found"] is True
    assert len(result["findings"]) == 2


def test_clean_environment():
    engine = AutonomousThreatHuntingEngine()

    result = engine.analyze_hunting_result({})

    assert result["threat_found"] is False


def test_record_hunt_history():
    engine = AutonomousThreatHuntingEngine()

    result = engine.record_hunt(
        "Malware Persistence",
        "No threat detected"
    )

    assert result["outcome"] == "No threat detected"


def test_hunting_history():
    engine = AutonomousThreatHuntingEngine()

    history = engine.get_hunting_history()

    assert "hypotheses" in history
    assert "results" in history
    assert "history" in history