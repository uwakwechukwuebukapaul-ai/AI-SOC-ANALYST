from services.response.autonomous_response_executor import (
    AutonomousResponseExecutor
)


def test_execute_response():

    executor = AutonomousResponseExecutor()

    result = executor.execute_response({
        "investigation_id": "INC-001",
        "actions": [
            "block_ioc",
            "notify_analyst"
        ]
    })

    assert result["status"] == "completed"
    assert "block_ioc" in result["actions"]


def test_execute_single_action():

    executor = AutonomousResponseExecutor()

    result = executor.execute_single_action(
        "isolate_endpoint"
    )

    assert result["success"] is True


def test_failed_action():

    executor = AutonomousResponseExecutor()

    result = executor.execute_single_action(
        "unknown_action"
    )

    assert result["success"] is False


def test_partial_failure():

    executor = AutonomousResponseExecutor()

    result = executor.execute_response({
        "investigation_id": "INC-002",
        "actions": [
            "block_ioc",
            "invalid_action"
        ]
    })

    assert result["status"] == "partial_failure"


def test_execution_history():

    executor = AutonomousResponseExecutor()

    executor.execute_response({
        "investigation_id": "INC-003",
        "actions": [
            "notify_analyst"
        ]
    })

    assert len(
        executor.get_execution_history()
    ) == 1


def test_clear_history():

    executor = AutonomousResponseExecutor()

    executor.execute_response({
        "investigation_id": "INC-004",
        "actions": [
            "monitor_activity"
        ]
    })

    executor.clear_history()

    assert len(
        executor.get_execution_history()
    ) == 0