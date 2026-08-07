"""
Integration tests for the end-to-end investigation
execution orchestrator.
"""

from __future__ import annotations

from services.investigation_intelligence import (
    InvestigationEngine,
)
from services.investigation_runtime.execution import (
    InvestigationExecutionOrchestrator,
)
from services.investigation_runtime.integration import (
    InvestigationServiceBridge,
)


def test_orchestrator_executes_all_runtime_services():
    bridge = InvestigationServiceBridge()

    bridge.register_executor(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "risk_score": 92,
            "severity": "critical",
            "status": "completed",
        },
    )

    bridge.register_executor(
        name="detection",
        capability="detection_analysis",
        executor=lambda investigation: {
            "matches": [
                "suspicious_powershell",
            ],
            "status": "completed",
        },
    )

    bridge.register_executor(
        name="mitre",
        capability="attack_mapping",
        executor=lambda investigation: {
            "techniques": [
                "T1059",
            ],
            "status": "completed",
        },
    )

    bridge.register_executor(
        name="threat_hunting",
        capability="threat_hunting",
        executor=lambda investigation: {
            "matches": [
                "powershell_execution",
            ],
            "status": "completed",
        },
    )

    orchestrator = (
        InvestigationExecutionOrchestrator(
            service_bridge=bridge,
            intelligence_engine=InvestigationEngine(),
        )
    )

    investigation = {
        "source": "endpoint",
        "indicator": "powershell",
    }

    result = orchestrator.execute(
        investigation
    )

    assert result["status"] == "completed"

    assert result["execution"]["executed"] == [
        "risk",
        "detection",
        "mitre",
        "threat_hunting",
    ]

    assert result["execution"]["failed"] == []

    assert result["intelligence"]["risk"][
        "severity"
    ] == "critical"

    assert "T1059" in result[
        "intelligence"
    ]["mitre"]["techniques"]

    assert result[
        "intelligence"
    ]["detection"]["matches"] == [
        "suspicious_powershell"
    ]

    assert result[
        "finding"
    ]["finding_count"] >= 3

    assert result[
        "confidence"
    ]["score"] > 0

    assert result[
        "correlation"
    ]["signal_count"] > 0


def test_orchestrator_handles_provider_failure():
    bridge = InvestigationServiceBridge()

    bridge.register_executor(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "risk_score": 80,
            "severity": "high",
        },
    )

    def failing_provider(
        investigation,
    ):
        raise RuntimeError(
            "Provider unavailable"
        )

    bridge.register_executor(
        name="detection",
        capability="detection_analysis",
        executor=failing_provider,
    )

    orchestrator = (
        InvestigationExecutionOrchestrator(
            service_bridge=bridge,
            intelligence_engine=InvestigationEngine(),
        )
    )

    result = orchestrator.execute(
        {
            "source": "endpoint",
            "indicator": "powershell",
        }
    )

    assert result["status"] == (
        "completed_with_errors"
    )

    assert result["execution"]["executed"] == [
        "risk",
    ]

    assert result["execution"]["failed"] == [
        "detection",
    ]

    assert len(result["errors"]) == 1

    assert result["errors"][0][
        "service"
    ] == "detection"

    assert result["intelligence"]["risk"][
        "severity"
    ] == "high"


def test_orchestrator_rejects_empty_investigation():
    bridge = InvestigationServiceBridge()

    orchestrator = (
        InvestigationExecutionOrchestrator(
            service_bridge=bridge,
            intelligence_engine=InvestigationEngine(),
        )
    )

    try:
        orchestrator.execute({})
    except ValueError as exc:
        assert str(exc) == (
            "Investigation cannot be empty."
        )
    else:
        raise AssertionError(
            "Expected ValueError"
        )


def test_orchestrator_preserves_investigation():
    bridge = InvestigationServiceBridge()

    bridge.register_executor(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "risk_score": 50,
        },
    )

    orchestrator = (
        InvestigationExecutionOrchestrator(
            service_bridge=bridge,
            intelligence_engine=InvestigationEngine(),
        )
    )

    investigation = {
        "case_id": "INC-TEST-001",
        "source": "email",
        "indicator": "malicious.example",
    }

    result = orchestrator.execute(
        investigation
    )

    assert result[
        "investigation"
    ] == investigation

    assert result[
        "finding"
    ]["investigation"] == investigation