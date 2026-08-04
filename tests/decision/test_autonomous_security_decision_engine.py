from services.decision.autonomous_security_decision_engine import (
    AutonomousSecurityDecisionEngine
)


def test_high_risk_decision():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.evaluate_threat({
        "risk_score": 95,
        "threat_type": "credential_theft",
        "asset": "finance-laptop"
    })

    assert result["severity"] == "critical"



def test_medium_risk_decision():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.evaluate_threat({
        "risk_score": 50,
        "threat_type": "suspicious_activity"
    })

    assert result["severity"] == "medium"



def test_low_risk_decision():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.evaluate_threat({
        "risk_score": 10,
        "threat_type": "unknown"
    })

    assert result["severity"] == "low"



def test_response_priority():

    engine = AutonomousSecurityDecisionEngine()

    decision = engine.evaluate_threat({
        "risk_score": 98,
        "threat_type": "malware"
    })

    priority = engine.generate_response_priority(decision)

    assert priority == "immediate"



def test_auto_response_detection():

    engine = AutonomousSecurityDecisionEngine()

    decision = engine.evaluate_threat({
        "risk_score": 92,
        "threat_type": "ransomware"
    })

    assert engine.should_auto_respond(decision)



def test_decision_history():

    engine = AutonomousSecurityDecisionEngine()

    engine.evaluate_threat({
        "risk_score": 80,
        "threat_type": "phishing"
    })

    history = engine.get_decision_history()

    assert len(history) == 1