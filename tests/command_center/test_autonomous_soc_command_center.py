from services.command_center.autonomous_soc_command_center import (
    AutonomousSOCCommandCenter
)


def test_dashboard_snapshot():

    center = AutonomousSOCCommandCenter()

    center.register_agent_status(
        "Threat Hunter",
        "online"
    )

    snapshot = center.get_dashboard_snapshot()

    assert snapshot["agents"] == 1


def test_agent_visibility():

    center = AutonomousSOCCommandCenter()

    agent = center.register_agent_status(
        "Detection Agent",
        "active"
    )

    assert (
        agent["status"]
        ==
        "active"
    )


def test_active_investigations():

    center = AutonomousSOCCommandCenter()

    investigation = center.add_investigation(
        "INC-001",
        "critical"
    )

    assert (
        investigation["status"]
        ==
        "active"
    )


def test_threat_overview():

    center = AutonomousSOCCommandCenter()

    threat = center.add_threat_event(
        "malware",
        95
    )

    assert (
        threat["risk_score"]
        ==
        95
    )


def test_system_health():

    center = AutonomousSOCCommandCenter()

    health = center.get_system_health()

    assert (
        health["status"]
        ==
        "healthy"
    )


def test_command_history():

    center = AutonomousSOCCommandCenter()

    center.register_agent_status(
        "SOC Agent",
        "online"
    )

    history = center.get_history()

    assert len(history) == 1