from services.copilot.autonomous_soc_copilot_engine import (
    AutonomousSOCCopilotEngine
)


def test_analyze_security_question():

    copilot = AutonomousSOCCopilotEngine()

    result = copilot.analyze_security_question(
        "Is this phishing?"
    )

    assert "analysis" in result


def test_generate_investigation_summary():

    copilot = AutonomousSOCCopilotEngine()

    result = copilot.generate_investigation_summary(
        "INC-001",
        [
            "malicious URL",
            "suspicious domain"
        ]
    )

    assert (
        result["investigation_id"]
        ==
        "INC-001"
    )


def test_explain_threat():

    copilot = AutonomousSOCCopilotEngine()

    result = copilot.explain_threat(
        "ransomware",
        "critical"
    )

    assert (
        result["severity"]
        ==
        "critical"
    )


def test_recommend_response():

    copilot = AutonomousSOCCopilotEngine()

    result = copilot.recommend_response(
        "malware"
    )

    assert len(
        result["actions"]
    ) > 0


def test_generate_report():

    copilot = AutonomousSOCCopilotEngine()

    result = copilot.generate_report(
        "INC-100",
        "Threat contained"
    )

    assert (
        result["incident_id"]
        ==
        "INC-100"
    )


def test_copilot_history():

    copilot = AutonomousSOCCopilotEngine()

    copilot.analyze_security_question(
        "Explain IOC"
    )

    history = copilot.get_history()

    assert len(history) == 1