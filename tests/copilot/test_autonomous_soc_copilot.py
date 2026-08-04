from services.copilot.autonomous_soc_copilot import (
    AutonomousSOCCopilot
)


def test_analyze_incident():

    copilot = AutonomousSOCCopilot()

    result = copilot.analyze_incident(
        "INC001",
        {
            "malware": True,
            "credential_compromise": True
        }
    )

    assert result["risk_level"] == "CRITICAL"


def test_generate_recommendation():

    copilot = AutonomousSOCCopilot()

    analysis = copilot.analyze_incident(
        "INC002",
        {
            "malware": True
        }
    )

    recommendation = copilot.generate_recommendation(
        analysis
    )

    assert "recommendation" in recommendation


def test_explain_incident():

    copilot = AutonomousSOCCopilot()

    analysis = copilot.analyze_incident(
        "INC003",
        {
            "suspicious_network": True
        }
    )

    explanation = copilot.explain_incident(
        analysis
    )

    assert explanation["incident_id"] == "INC003"


def test_similar_pattern_search():

    copilot = AutonomousSOCCopilot()

    copilot.analyze_incident(
        "INC004",
        {
            "malware": True
        }
    )

    results = copilot.find_similar_patterns(
        "malware"
    )

    assert len(results) == 1


def test_history_tracking():

    copilot = AutonomousSOCCopilot()

    copilot.analyze_incident(
        "INC005",
        {}
    )

    history = copilot.get_history()

    assert len(history) == 1


def test_clear_history():

    copilot = AutonomousSOCCopilot()

    copilot.analyze_incident(
        "INC006",
        {}
    )

    copilot.clear_history()

    assert len(copilot.history) == 0