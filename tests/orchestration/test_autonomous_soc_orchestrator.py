from services.orchestration.autonomous_soc_orchestrator import (
    AutonomousSOCOrchestrator
)


def test_create_workflow():
    engine = AutonomousSOCOrchestrator()

    workflow = engine.create_workflow(
        "INC-001"
    )

    assert workflow["incident_id"] == "INC-001"
    assert workflow["status"] == "created"


def test_execute_single_step():
    engine = AutonomousSOCOrchestrator()

    workflow = engine.create_workflow(
        "INC-002"
    )

    updated = engine.execute_step(
        workflow,
        "detection"
    )

    assert "detection" in updated["completed_steps"]


def test_execute_full_pipeline():
    engine = AutonomousSOCOrchestrator()

    workflow = engine.create_workflow(
        "INC-003"
    )

    result = engine.execute_pipeline(
        workflow
    )

    assert result["status"] == "completed"


def test_pipeline_status():
    engine = AutonomousSOCOrchestrator()

    workflow = engine.create_workflow(
        "INC-004"
    )

    status = engine.get_pipeline_status(
        workflow
    )

    assert status["remaining"] == 10


def test_failure_detection():
    engine = AutonomousSOCOrchestrator()

    workflow = engine.create_workflow(
        "INC-005"
    )

    failure = engine.detect_failure(
        workflow,
        "response_execution"
    )

    assert failure["status"] == "requires_review"


def test_orchestration_history():
    engine = AutonomousSOCOrchestrator()

    engine.create_workflow(
        "INC-006"
    )

    assert len(engine.get_history()) == 1