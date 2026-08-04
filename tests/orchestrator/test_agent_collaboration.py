from services.orchestrator.agent_collaboration import (
    AgentCollaboration,
)


def test_register_collaboration_group():

    collaboration = AgentCollaboration()

    group = collaboration.register_collaboration_group(
        "incident_response_team"
    )

    assert group["status"] == "active"
    assert "agents" in group



def test_add_agent_to_group():

    collaboration = AgentCollaboration()

    collaboration.register_collaboration_group(
        "soc_team"
    )

    group = collaboration.add_agent_to_group(
        "soc_team",
        "threat_agent"
    )

    assert "threat_agent" in group["agents"]



def test_execute_collaboration():

    collaboration = AgentCollaboration()

    collaboration.register_collaboration_group(
        "investigation_team"
    )

    collaboration.add_agent_to_group(
        "investigation_team",
        "ioc_agent"
    )

    result = collaboration.execute_collaboration(
        "investigation_team",
        "Analyze phishing incident"
    )

    assert result["status"] == "completed"
    assert result["task"] == "Analyze phishing incident"



def test_agent_message_exchange():

    collaboration = AgentCollaboration()

    collaboration.register_collaboration_group(
        "analysis_team"
    )

    message = collaboration.send_message(
        "analysis_team",
        "risk_agent",
        "ioc_agent",
        "Check suspicious domain"
    )

    assert message["sender"] == "risk_agent"
    assert message["receiver"] == "ioc_agent"



def test_collaboration_history():

    collaboration = AgentCollaboration()

    collaboration.register_collaboration_group(
        "response_team"
    )

    collaboration.execute_collaboration(
        "response_team",
        "Contain malware"
    )

    history = collaboration.get_collaboration_history()

    assert len(history) == 1



def test_clear_history():

    collaboration = AgentCollaboration()

    collaboration.register_collaboration_group(
        "cleanup_team"
    )

    collaboration.execute_collaboration(
        "cleanup_team",
        "Remove threat"
    )

    collaboration.clear_history()

    assert collaboration.get_collaboration_history() == []