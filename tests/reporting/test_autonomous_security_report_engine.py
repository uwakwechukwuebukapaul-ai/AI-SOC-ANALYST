from services.reporting.autonomous_security_report_engine import (
    AutonomousSecurityReportEngine
)


def test_generate_report():
    engine = AutonomousSecurityReportEngine()

    report = engine.generate_report(
        "INC-001",
        ["malware detected"],
        90
    )

    assert report["incident_id"] == "INC-001"
    assert report["status"] == "generated"


def test_generate_summary():
    engine = AutonomousSecurityReportEngine()

    report = engine.generate_report(
        "INC-002",
        ["credential theft"],
        70
    )

    summary = engine.generate_summary(report)

    assert summary["finding_count"] == 1


def test_executive_summary_critical():
    engine = AutonomousSecurityReportEngine()

    report = engine.generate_report(
        "INC-003",
        ["ransomware"],
        95
    )

    summary = engine.generate_executive_summary(report)

    assert summary["severity"] == "CRITICAL"


def test_add_timeline_event():
    engine = AutonomousSecurityReportEngine()

    report = engine.generate_report(
        "INC-004",
        [],
        20
    )

    updated = engine.add_timeline_event(
        report,
        "Initial detection"
    )

    assert len(updated["timeline"]) == 1


def test_report_history():
    engine = AutonomousSecurityReportEngine()

    engine.generate_report(
        "INC-005",
        [],
        10
    )

    assert len(engine.get_report_history()) == 1


def test_clear_history():
    engine = AutonomousSecurityReportEngine()

    engine.generate_report(
        "INC-006",
        [],
        10
    )

    engine.clear_history()

    assert len(engine.get_report_history()) == 0