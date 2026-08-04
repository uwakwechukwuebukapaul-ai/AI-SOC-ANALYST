from services.investigation.autonomous_investigation_engine import (
    AutonomousInvestigationEngine
)


def test_create_investigation():

    engine = AutonomousInvestigationEngine()

    result = engine.create_investigation(
        "Suspicious PowerShell execution"
    )

    assert result["status"] == "active"
    assert result["alert"] == (
        "Suspicious PowerShell execution"
    )


def test_collect_evidence():

    engine = AutonomousInvestigationEngine()

    investigation = engine.create_investigation(
        "Malware alert"
    )

    result = engine.collect_evidence(
        investigation["id"],
        "malware hash detected"
    )

    assert result["status"] == "collected"
    assert result["evidence_count"] == 1


def test_correlate_intelligence():

    engine = AutonomousInvestigationEngine()

    investigation = engine.create_investigation(
        "Phishing attempt"
    )

    result = engine.correlate_intelligence(
        investigation["id"],
        "APT28 indicator"
    )

    assert result["matched"] is True
    assert result["confidence"] == "high"


def test_generate_investigation_report():

    engine = AutonomousInvestigationEngine()

    investigation = engine.create_investigation(
        "Credential theft"
    )

    result = engine.generate_report(
        investigation["id"]
    )

    assert "summary" in result
    assert result["confidence"] == "high"


def test_confidence_scoring():

    engine = AutonomousInvestigationEngine()

    investigation = engine.create_investigation(
        "Ransomware"
    )

    engine.collect_evidence(
        investigation["id"],
        "encrypted files"
    )

    engine.correlate_intelligence(
        investigation["id"],
        "ransomware family"
    )

    result = engine.calculate_confidence(
        investigation["id"]
    )

    assert result["score"] == 100


def test_investigation_history():

    engine = AutonomousInvestigationEngine()

    engine.create_investigation(
        "Suspicious login"
    )

    assert len(engine.get_history()) == 1