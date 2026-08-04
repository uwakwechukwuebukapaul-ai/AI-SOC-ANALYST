from services.prediction.autonomous_security_prediction_engine import (
    AutonomousSecurityPredictionEngine
)


def test_create_prediction():

    engine = AutonomousSecurityPredictionEngine()

    prediction = engine.create_prediction(
        "ransomware",
        [
            "malware_activity"
        ]
    )

    assert prediction["threat_type"] == "ransomware"


def test_attack_probability_prediction():

    engine = AutonomousSecurityPredictionEngine()

    result = engine.predict_attack_probability(
        [
            "malware_activity",
            "credential_compromise"
        ]
    )

    assert result["attack_probability"] == 60
    assert result["risk_level"] == "high"


def test_risk_trajectory_analysis():

    engine = AutonomousSecurityPredictionEngine()

    result = engine.analyze_risk_trajectory(
        90,
        50
    )

    assert result["trajectory"] == "increasing"


def test_attacker_behavior_prediction():

    engine = AutonomousSecurityPredictionEngine()

    result = engine.predict_attacker_behavior(
        "credential_access"
    )

    assert (
        result["predicted_behavior"]
        ==
        "privilege_escalation"
    )


def test_defense_recommendation():

    engine = AutonomousSecurityPredictionEngine()

    result = engine.generate_defense_recommendation(
        "critical"
    )

    assert "incident response" in (
        result["recommendation"]
    )


def test_prediction_history():

    engine = AutonomousSecurityPredictionEngine()

    engine.create_prediction(
        "phishing",
        [
            "email_indicator"
        ]
    )

    history = engine.get_history()

    assert len(history) == 1