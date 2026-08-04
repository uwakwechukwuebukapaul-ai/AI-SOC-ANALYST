from services.agents.autonomous_security_agent_supervisor import (
    AutonomousSecurityAgentSupervisor
)


def test_register_agent():

    supervisor = AutonomousSecurityAgentSupervisor()

    agent = supervisor.register_agent(
        "agent-001",
        "Threat Hunter",
        "threat_hunting"
    )

    assert agent["status"] == "healthy"


def test_update_agent_health():

    supervisor = AutonomousSecurityAgentSupervisor()

    supervisor.register_agent(
        "agent-002",
        "Detection Agent",
        "detection"
    )

    agent = supervisor.update_agent_health(
        "agent-002",
        "degraded",
        0.6
    )

    assert agent["confidence"] == 0.6


def test_analyze_agent_health():

    supervisor = AutonomousSecurityAgentSupervisor()

    supervisor.register_agent(
        "agent-003",
        "Response Agent",
        "response"
    )

    result = supervisor.analyze_agent_health(
        "agent-003"
    )

    assert result["condition"] == "healthy"


def test_detect_failures():

    supervisor = AutonomousSecurityAgentSupervisor()

    supervisor.register_agent(
        "agent-004",
        "SOAR Agent",
        "soar"
    )

    supervisor.update_agent_health(
        "agent-004",
        "failed",
        0.2
    )

    failures = supervisor.detect_failures()

    assert len(failures) == 1


def test_generate_recovery_action():

    supervisor = AutonomousSecurityAgentSupervisor()

    supervisor.register_agent(
        "agent-005",
        "Investigation Agent",
        "investigation"
    )

    supervisor.update_agent_health(
        "agent-005",
        "failed",
        0.1
    )

    recovery = supervisor.generate_recovery_action(
        "agent-005"
    )

    assert recovery["action"] == "restart_agent"


def test_supervisor_history():

    supervisor = AutonomousSecurityAgentSupervisor()

    supervisor.register_agent(
        "agent-006",
        "Learning Agent",
        "learning"
    )

    history = supervisor.supervisor_history()

    assert len(history) > 0