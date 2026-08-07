"""
API Gateway Integration Tests

Validates external request flow into Sentinel DNA.
"""


from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)


def test_api_request_bootstrap():

    coordinator = AutonomousAgentCoordinator()

    assert coordinator is not None


def test_alert_ingestion_flow():

    coordinator = AutonomousAgentCoordinator()

    alert = {
        "source": "endpoint",
        "severity": "high",
        "event": "suspicious_login"
    }

    workflow = coordinator.coordinate_workflow(
        [
            "ingest_alert",
            "normalize_event",
            "start_investigation"
        ]
    )

    assert workflow["status"] == "completed"
    assert len(workflow["steps"]) == 3


def test_external_security_source_routing():

    coordinator = AutonomousAgentCoordinator()

    result = coordinator.route_intelligence_request(
        "threat_detection"
    )

    assert result["assigned_agent"] == "detection_agent"


def test_unknown_request_fallback():

    coordinator = AutonomousAgentCoordinator()

    result = coordinator.route_intelligence_request(
        "unknown"
    )

    assert result["assigned_agent"] == "general_security_agent"


def test_platform_health_status():

    coordinator = AutonomousAgentCoordinator()

    status = coordinator.system_status()

    assert status["status"] == "operational"