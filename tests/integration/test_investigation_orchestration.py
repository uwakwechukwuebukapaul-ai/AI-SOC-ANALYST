"""
Unified investigation orchestration integration tests.
"""

from services.orchestration import (
    InvestigationContext,
    InvestigationOrchestrator,
    WorkflowState,
)


def test_investigation_context():
    context = InvestigationContext(
        case_id="INC-20260807-001",
        alert={
            "type": "suspicious_login",
            "severity": "high",
        },
    )

    context.add_timeline_event(
        "alert_received"
    )

    snapshot = context.snapshot()

    assert snapshot["case_id"] == "INC-20260807-001"
    assert snapshot["alert"]["severity"] == "high"
    assert len(snapshot["timeline"]) == 1


def test_workflow_state():
    assert WorkflowState.CREATED.value == "created"
    assert WorkflowState.ANALYZING.value == "analyzing"
    assert WorkflowState.COMPLETED.value == "completed"


def test_step_registration():
    orchestrator = InvestigationOrchestrator()

    orchestrator.register_step(
        "analysis",
        lambda context: {
            "evidence_type": "authentication",
            "risk_signal": "credential_attack",
        },
    )

    assert "analysis" in orchestrator.registered_steps()


def test_unified_investigation_flow():
    orchestrator = InvestigationOrchestrator()

    orchestrator.register_step(
        "analysis",
        lambda context: {
            "event": context.alert["type"],
            "severity": context.alert["severity"],
        },
    )

    orchestrator.register_step(
        "enrichment",
        lambda context: {
            "reputation": "suspicious",
            "source": "threat_intelligence",
        },
    )

    orchestrator.register_step(
        "decision",
        lambda context: {
            "decision": "investigate",
            "confidence": 0.91,
        },
    )

    orchestrator.register_step(
        "response",
        lambda context: {
            "action": "notify_analyst",
            "status": "simulated",
        },
    )

    result = orchestrator.run(
        case_id="INC-20260807-001",
        alert={
            "type": "credential_attack",
            "severity": "high",
        },
    )

    assert result["state"] == "completed"
    assert result["case_id"] == "INC-20260807-001"

    investigation = result["investigation"]

    assert len(investigation["evidence"]) == 1
    assert investigation["threat_intelligence"]["reputation"] == "suspicious"
    assert len(investigation["decisions"]) == 1
    assert investigation["response"]["status"] == "simulated"


def test_execution_trace():
    orchestrator = InvestigationOrchestrator()

    orchestrator.register_step(
        "analysis",
        lambda context: {"status": "analyzed"},
    )

    result = orchestrator.run(
        case_id="INC-TRACE-001",
        alert={"type": "test"},
    )

    assert result["state"] == "completed"
    assert len(result["trace"]) >= 3