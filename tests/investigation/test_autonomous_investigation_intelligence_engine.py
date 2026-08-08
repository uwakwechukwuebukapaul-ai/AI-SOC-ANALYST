from services.investigation.autonomous_investigation_intelligence_engine import (
    AutonomousInvestigationIntelligenceEngine,
)


def test_create_investigation():
    engine = AutonomousInvestigationIntelligenceEngine()

    result = engine.create_investigation(
        "INC-001",
        "phishing",
        "high",
    )

    assert result["status"] == "active"


def test_analyze_evidence():
    engine = AutonomousInvestigationIntelligenceEngine()

    engine.create_investigation(
        "INC-001",
        "phishing",
        "high",
    )

    result = engine.analyze_evidence(
        "INC-001",
        ["email", "url", "attachment"],
    )

    assert result["evidence_count"] == 3


def test_correlate_threat_activity():
    engine = AutonomousInvestigationIntelligenceEngine()

    result = engine.correlate_threat_activity(
        ["8.8.8.8", "malicious.com"],
    )

    assert result["risk_level"] == "HIGH"


def test_generate_investigation_summary():
    engine = AutonomousInvestigationIntelligenceEngine()

    engine.create_investigation(
        "INC-001",
        "phishing",
        "high",
    )

    result = engine.generate_investigation_summary(
        "INC-001",
    )

    assert "summary" in result


def test_generate_timeline():
    engine = AutonomousInvestigationIntelligenceEngine()

    engine.create_investigation(
        "INC-001",
        "phishing",
        "high",
    )

    result = engine.generate_timeline(
        "INC-001",
    )

    assert len(result["events"]) == 3


def test_investigation_history():
    engine = AutonomousInvestigationIntelligenceEngine()

    engine.create_investigation(
        "INC-001",
        "malware",
        "critical",
    )

    history = engine.get_investigation_history()

    assert len(history) == 1