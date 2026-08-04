from services.orchestrator.autonomous_orchestrator import AutonomousOrchestrator


def test_create_investigation_plan():
    orchestrator = AutonomousOrchestrator()

    plan = orchestrator.create_plan(
        "Investigate phishing campaign"
    )

    assert plan["objective"] == "Investigate phishing campaign"
    assert plan["status"] == "created"


def test_select_agents():
    orchestrator = AutonomousOrchestrator()

    agents = orchestrator.select_agents(
        "threat_analysis"
    )

    assert len(agents) > 0


def test_execute_workflow():
    orchestrator = AutonomousOrchestrator()

    plan = orchestrator.create_plan(
        "Analyze suspicious activity"
    )

    result = orchestrator.execute(plan)

    assert result["status"] == "completed"


def test_handle_agent_failure():
    orchestrator = AutonomousOrchestrator()

    result = orchestrator.handle_failure(
        "analysis_agent",
        "timeout"
    )

    assert result["status"] == "handled"


def test_collect_results():
    orchestrator = AutonomousOrchestrator()

    results = orchestrator.collect_results(
        {
            "finding": "malware detected"
        }
    )

    assert len(results) == 1


def test_learning_feedback_loop():
    orchestrator = AutonomousOrchestrator()

    result = orchestrator.learn_from_execution(
        {
            "success": True
        }
    )

    assert result["learned"] is True


def test_orchestrator_history():
    orchestrator = AutonomousOrchestrator()

    orchestrator.create_plan(
        "Threat investigation"
    )

    history = orchestrator.get_history()

    assert len(history) == 1