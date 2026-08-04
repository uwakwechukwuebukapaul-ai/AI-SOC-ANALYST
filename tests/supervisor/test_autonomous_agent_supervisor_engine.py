from services.supervisor.autonomous_agent_supervisor_engine import (
    AutonomousAgentSupervisorEngine
)


def test_register_agent():

    engine = AutonomousAgentSupervisorEngine()

    agent = engine.register_agent(
        "Threat Hunter Agent",
        "hunting"
    )

    assert (
        agent["status"]
        ==
        "active"
    )


def test_monitor_agent_health():

    engine = AutonomousAgentSupervisorEngine()

    agent = engine.register_agent(
        "Detection Agent",
        "detection"
    )

    result = engine.monitor_agent_health(
        agent["id"]
    )

    assert (
        result["health"]
        ==
        "healthy"
    )


def test_assign_priority():

    engine = AutonomousAgentSupervisorEngine()

    result = engine.assign_priority(
        "critical investigation",
        95
    )

    assert (
        result["priority"]
        ==
        "critical"
    )


def test_agent_failure_recovery():

    engine = AutonomousAgentSupervisorEngine()

    agent = engine.register_agent(
        "Response Agent",
        "soar"
    )

    result = engine.recover_failed_agent(
        agent["id"]
    )

    assert (
        result["recovery"]
        ==
        "successful"
    )


def test_agent_performance_score():

    engine = AutonomousAgentSupervisorEngine()

    agent = engine.register_agent(
        "AI Analyst",
        "investigation"
    )

    result = engine.evaluate_agent_performance(
        agent["id"],
        8,
        2
    )

    assert (
        result["performance_score"]
        ==
        80.0
    )


def test_supervisor_history():

    engine = AutonomousAgentSupervisorEngine()

    engine.register_agent(
        "Memory Agent",
        "learning"
    )

    history = engine.get_history()

    assert len(history) == 1