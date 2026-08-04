from services.response.autonomous_response_planner import (
    AutonomousResponsePlanner
)


def test_create_response_plan():

    planner = AutonomousResponsePlanner()

    result = planner.create_response_plan({
        "id": "INC-001",
        "risk": "CRITICAL"
    })

    assert result["risk"] == "CRITICAL"
    assert "isolate_endpoint" in result["actions"]


def test_high_risk_response():

    planner = AutonomousResponsePlanner()

    result = planner.create_response_plan({
        "id": "INC-002",
        "risk": "HIGH"
    })

    assert "block_ioc" in result["actions"]


def test_low_risk_response():

    planner = AutonomousResponsePlanner()

    result = planner.create_response_plan({
        "id": "INC-003",
        "risk": "LOW"
    })

    assert "close_as_low_risk" in result["actions"]


def test_action_priority():

    planner = AutonomousResponsePlanner()

    score = planner.evaluate_action_priority(
        "isolate_endpoint"
    )

    assert score == 100


def test_response_history():

    planner = AutonomousResponsePlanner()

    planner.create_response_plan({
        "id": "INC-004",
        "risk": "MEDIUM"
    })

    history = planner.get_response_history()

    assert len(history) == 1


def test_clear_history():

    planner = AutonomousResponsePlanner()

    planner.create_response_plan({
        "id": "INC-005",
        "risk": "HIGH"
    })

    planner.clear_history()

    assert len(planner.get_response_history()) == 0