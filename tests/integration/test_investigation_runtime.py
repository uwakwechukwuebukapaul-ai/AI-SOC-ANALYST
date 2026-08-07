"""
Integration tests for the Unified Investigation Runtime.
"""

from services.investigation_runtime import (
    DecisionGate,
    DecisionOutcome,
    InvestigationPipeline,
    InvestigationRuntime,
    InvestigationStage,
    ServiceRegistry,
)


class FakeRiskService:
    def analyze(self, evidence):
        return {
            "risk_score": 0.90,
            "risk_level": "critical",
        }


class FakeMitreService:
    def analyze(self, evidence):
        return {
            "techniques": ["T1059"],
            "tactics": ["Execution"],
        }


class FakeDetectionService:
    def analyze(self, evidence):
        return {
            "detections": ["suspicious_command_execution"],
        }


def test_service_registry():
    registry = ServiceRegistry()

    service = FakeRiskService()

    registry.register("risk", service)

    assert registry.has("risk")
    assert registry.get("risk") is service
    assert "risk" in registry.names()


def test_decision_gate():
    gate = DecisionGate()

    decision = gate.evaluate(
        {
            "risk_score": 0.95,
            "confidence": 0.90,
            "response_authorized": True,
        }
    )

    assert decision == DecisionOutcome.RESPOND


def test_decision_gate_reads_risk_stage():
    gate = DecisionGate()

    decision = gate.evaluate(
        {
            "stages": {
                "risk": {
                    "risk_score": 0.90,
                    "confidence": 0.95,
                }
            }
        }
    )

    assert decision == DecisionOutcome.ESCALATE


def test_pipeline_execution():
    pipeline = InvestigationPipeline()

    pipeline.register(
        InvestigationStage.RISK,
        lambda context: {
            "risk_score": 0.80,
        },
        required=True,
    )

    pipeline.register(
        InvestigationStage.MITRE,
        lambda context: {
            "techniques": ["T1059"],
        },
    )

    results = pipeline.execute(
        {
            "evidence": {
                "command": "powershell",
            }
        }
    )

    assert len(results) == 2
    assert results[0].successful
    assert results[1].successful


def test_unified_investigation_runtime():
    runtime = InvestigationRuntime()

    runtime.register_stage(
        InvestigationStage.RISK,
        lambda context: {
            "risk_score": 0.90,
            "confidence": 0.95,
        },
        required=True,
    )

    runtime.register_stage(
        InvestigationStage.MITRE,
        lambda context: {
            "techniques": ["T1059"],
        },
    )

    runtime.register_stage(
        InvestigationStage.DETECTION,
        lambda context: {
            "matches": [
                "suspicious_powershell",
            ],
        },
    )

    result = runtime.investigate(
        {
            "source": "endpoint",
            "indicator": "powershell",
        },
        metadata={
            "tenant": "test-tenant",
        },
    )

    assert result.successful
    assert result.investigation_id.startswith("INV-")
    assert result.status == "completed"
    assert len(result.stages) == 3

    assert result.decision == "escalate"


def test_runtime_serialization():
    runtime = InvestigationRuntime()

    runtime.register_stage(
        InvestigationStage.RISK,
        lambda context: {
            "risk_score": 0.20,
        },
    )

    result = runtime.investigate()

    payload = result.to_dict()

    assert payload["investigation_id"] == result.investigation_id
    assert payload["status"] == "completed"
    assert payload["stages"]