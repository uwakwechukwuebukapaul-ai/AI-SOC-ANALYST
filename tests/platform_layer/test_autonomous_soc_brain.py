from services.platform.autonomous_soc_brain import AutonomousSOCBrain


def test_process_security_event():

    brain = AutonomousSOCBrain()

    event = {
        "name": "Suspicious Login",
        "risk_score": 90,
        "indicators": [
            "multiple_failed_logins",
            "unknown_ip"
        ]
    }

    result = brain.process_security_event(event)

    assert result["status"] == "completed"
    assert result["decision"]["risk_level"] == "CRITICAL"


def test_low_risk_event():

    brain = AutonomousSOCBrain()

    event = {
        "name": "Normal Activity",
        "risk_score": 10,
        "indicators": []
    }

    result = brain.process_security_event(event)

    assert result["decision"]["recommended_action"] == "close"


def test_risk_classification():

    brain = AutonomousSOCBrain()

    assert brain._calculate_risk(90) == "CRITICAL"
    assert brain._calculate_risk(60) == "HIGH"
    assert brain._calculate_risk(30) == "MEDIUM"
    assert brain._calculate_risk(5) == "LOW"


def test_security_decision_generation():

    brain = AutonomousSOCBrain()

    investigation = {
        "risk_level": "HIGH"
    }

    decision = brain.make_security_decision(investigation)

    assert decision["recommended_action"] == "investigate_and_monitor"


def test_soc_status():

    brain = AutonomousSOCBrain()

    brain.process_security_event({
        "risk_score": 80,
        "indicators": ["malware"]
    })

    status = brain.get_soc_status()

    assert status["events_processed"] == 1
    assert status["investigations"] == 1


def test_clear_history():

    brain = AutonomousSOCBrain()

    brain.process_security_event({
        "risk_score": 70
    })

    result = brain.clear_history()

    assert result is True
    assert len(brain.events) == 0