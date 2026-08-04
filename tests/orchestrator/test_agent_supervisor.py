from services.orchestrator.agent_supervisor import AgentSupervisor


def test_register_agent():

    supervisor = AgentSupervisor()

    agent = supervisor.register_agent(
        "threat_classifier"
    )

    assert agent.agent_name == "threat_classifier"

    assert agent.status == "ACTIVE"



def test_record_execution():

    supervisor = AgentSupervisor()

    supervisor.register_agent(
        "ioc_agent"
    )

    agent = supervisor.record_execution(
        "ioc_agent"
    )

    assert agent.executions == 1

    assert agent.status == "ACTIVE"



def test_record_failure():

    supervisor = AgentSupervisor()

    supervisor.register_agent(
        "risk_engine"
    )

    agent = supervisor.record_failure(
        "risk_engine",
        "timeout"
    )

    assert agent.failures == 1

    assert agent.status == "DEGRADED"

    assert agent.last_error == "timeout"



def test_agent_health_lookup():

    supervisor = AgentSupervisor()

    supervisor.register_agent(
        "response_agent"
    )

    health = supervisor.get_health(
        "response_agent"
    )

    assert health["agent_name"] == "response_agent"



def test_reset_agent():

    supervisor = AgentSupervisor()

    supervisor.register_agent(
        "analysis_agent"
    )

    supervisor.record_failure(
        "analysis_agent",
        "model error"
    )

    agent = supervisor.reset_agent(
        "analysis_agent"
    )

    assert agent.status == "ACTIVE"

    assert agent.last_error is None