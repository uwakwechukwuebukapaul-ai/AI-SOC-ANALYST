from services.decision.autonomous_security_decision_engine import (
    AutonomousSecurityDecisionEngine
)


def test_create_decision():

    engine = AutonomousSecurityDecisionEngine()

    decision = engine.create_decision(
        "malware",
        95
    )

    assert decision["incident_type"] == "malware"


def test_risk_based_decision():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.evaluate_risk_decision(
        95
    )

    assert result["priority"] == "critical"
    assert (
        result["recommended_action"]
        ==
        "automatic_containment"
    )


def test_incident_priority():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.determine_incident_priority(
        10,
        9
    )

    assert result["priority"] == "critical"


def test_response_action_selection():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.select_response_action(
        "malware"
    )

    assert (
        result["action"]
        ==
        "isolate_endpoint"
    )


def test_human_approval_requirement():

    engine = AutonomousSecurityDecisionEngine()

    result = engine.requires_human_approval(
        "automatic_containment",
        0.80
    )

    assert (
        result["human_approval_required"]
        is True
    )


def test_decision_history():

    engine = AutonomousSecurityDecisionEngine()

    engine.create_decision(
        "phishing",
        60
    )

    history = engine.get_history()

    assert len(history) == 1