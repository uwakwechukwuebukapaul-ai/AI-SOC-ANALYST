from services.agents.autonomous_agent_supervisor import (
    AutonomousAgentSupervisor
)


def test_register_agent():

    supervisor = AutonomousAgentSupervisor()

    agent = supervisor.register_agent(
        "Detection Agent",
        [
            "alert analysis",
            "rule generation"
        ]
    )

    assert agent["name"] == "Detection Agent"
    assert agent["status"] == "active"



def test_get_agent():

    supervisor = AutonomousAgentSupervisor()

    supervisor.register_agent(
        "Hunting Agent",
        [
            "threat hunting"
        ]
    )

    agent = supervisor.get_agent(
        "Hunting Agent"
    )

    assert agent["name"] == "Hunting Agent"



def test_assign_task():

    supervisor = AutonomousAgentSupervisor()

    supervisor.register_agent(
        "SOAR Agent",
        [
            "automation"
        ]
    )

    result = supervisor.assign_task(
        "SOAR Agent",
        "execute containment playbook"
    )

    assert result["status"] == "assigned"



def test_execute_workflow():

    supervisor = AutonomousAgentSupervisor()

    supervisor.register_agent(
        "Reasoning Agent",
        [
            "analysis"
        ]
    )

    workflow = [
        {
            "agent": "Reasoning Agent",
            "task": "analyze incident"
        }
    ]

    result = supervisor.execute_workflow(
        workflow
    )

    assert result["workflow_status"] == "completed"
    assert len(result["steps"]) == 1



def test_agent_health_monitoring():

    supervisor = AutonomousAgentSupervisor()

    supervisor.register_agent(
        "Memory Agent",
        [
            "knowledge storage"
        ]
    )

    health = supervisor.monitor_agent_health()

    assert health["Memory Agent"]["healthy"] is True



def test_task_history():

    supervisor = AutonomousAgentSupervisor()

    supervisor.register_agent(
        "Copilot Agent",
        [
            "assistant reasoning"
        ]
    )

    supervisor.assign_task(
        "Copilot Agent",
        "summarize incident"
    )

    history = supervisor.get_task_history()

    assert len(history) == 1