"""
Integration tests for the Investigation Runtime service layer.
"""

from __future__ import annotations

import pytest

from services.investigation_runtime.adapters import (
    IntelligenceServiceAdapter,
)
from services.investigation_runtime.integration import (
    IntelligenceStageFactory,
    InvestigationServiceBridge,
    RuntimeServiceRegistry,
)
from services.investigation_runtime.investigation_pipeline import (
    InvestigationStage,
)


def test_runtime_service_registry():
    registry = RuntimeServiceRegistry()

    service = IntelligenceServiceAdapter(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "score": investigation.get("risk_score", 0),
        },
    )

    registry.register(service)

    assert registry.has("risk")
    assert registry.get("risk") is service
    assert registry.names() == ["risk"]
    assert registry.capabilities() == {
        "risk": "risk_assessment",
    }


def test_registry_rejects_duplicate_services():
    registry = RuntimeServiceRegistry()

    service = IntelligenceServiceAdapter(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {},
    )

    registry.register(service)

    with pytest.raises(ValueError):
        registry.register(service)


def test_bridge_registers_and_executes_service():
    bridge = InvestigationServiceBridge()

    bridge.register_executor(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "score": investigation["risk_score"],
            "status": "completed",
        },
    )

    result = bridge.execute(
        "risk",
        {
            "risk_score": 90,
        },
    )

    assert result["score"] == 90
    assert result["status"] == "completed"


def test_stage_factory_creates_runtime_handler():
    registry = RuntimeServiceRegistry()

    registry.register(
        IntelligenceServiceAdapter(
            name="mitre",
            capability="attack_mapping",
            executor=lambda investigation: {
                "techniques": ["T1059"],
            },
        )
    )

    factory = IntelligenceStageFactory(registry)

    handler = factory.create_handler("mitre")

    result = handler(
        {
            "indicator": "powershell",
        }
    )

    assert result["techniques"] == ["T1059"]


def test_stage_factory_creates_pipeline_step():
    registry = RuntimeServiceRegistry()

    registry.register(
        IntelligenceServiceAdapter(
            name="detection",
            capability="detection_analysis",
            executor=lambda investigation: {
                "matches": ["suspicious_powershell"],
            },
        )
    )

    factory = IntelligenceStageFactory(registry)

    step = factory.create_step(
        InvestigationStage.DETECTION,
        "detection",
    )

    assert step.stage == InvestigationStage.DETECTION
    assert callable(step.handler)
    assert step.required is False


def test_end_to_end_service_bridge_flow():
    bridge = InvestigationServiceBridge()

    bridge.register_executor(
        name="risk",
        capability="risk_assessment",
        executor=lambda investigation: {
            "score": 90,
            "severity": "critical",
        },
    )

    bridge.register_executor(
        name="mitre",
        capability="attack_mapping",
        executor=lambda investigation: {
            "techniques": ["T1059"],
            "tactics": ["Execution"],
        },
    )

    bridge.register_executor(
        name="detection",
        capability="detection_analysis",
        executor=lambda investigation: {
            "matches": [
                "suspicious_powershell",
            ],
        },
    )

    investigation = {
        "source": "endpoint",
        "indicator": "powershell",
    }

    risk = bridge.execute("risk", investigation)
    mitre = bridge.execute("mitre", investigation)
    detection = bridge.execute("detection", investigation)

    assert risk["severity"] == "critical"
    assert "T1059" in mitre["techniques"]
    assert "suspicious_powershell" in detection["matches"]

    assert bridge.available_services() == [
        "risk",
        "mitre",
        "detection",
    ]