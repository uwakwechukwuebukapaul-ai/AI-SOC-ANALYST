"""
Default intelligence provider registration.

This module is the composition boundary between the unified
Investigation Runtime and the existing Sentinel DNA intelligence
engines.

The individual engines remain independent. The runtime only sees
their normalized service contracts.
"""

from __future__ import annotations

from typing import Any

from services.detection_engineering.detection_engine import (
    DetectionEngine,
)
from services.mitre_intelligence.mitre_engine import (
    MitreIntelligenceEngine,
)
from services.risk.risk_intelligence_engine import (
    RiskIntelligenceEngine,
)
from services.threat_hunting.hunt_engine import (
    HuntEngine,
)

from ..integration import InvestigationServiceBridge


def _risk_executor(
    engine: RiskIntelligenceEngine,
    investigation: dict[str, Any],
) -> dict[str, Any]:
    """
    Execute the Risk Intelligence Engine.
    """

    return engine.assess(investigation)


def _mitre_executor(
    engine: MitreIntelligenceEngine,
    investigation: dict[str, Any],
) -> dict[str, Any]:
    """
    Execute the MITRE ATT&CK Intelligence Engine.
    """

    return engine.analyze(investigation)


def _detection_executor(
    engine: DetectionEngine,
    investigation: dict[str, Any],
) -> dict[str, Any]:
    """
    Execute the Detection Engineering Engine.
    """

    return engine.analyze_event(investigation)


def _hunting_executor(
    engine: HuntEngine,
    investigation: dict[str, Any],
) -> dict[str, Any]:
    """
    Execute the Threat Hunting Engine.

    The existing hunting engine expects a hypothesis and
    a dataset. The runtime normalizes the investigation
    into those inputs.
    """

    hypothesis = investigation.get(
        "hunt_hypothesis",
        {
            "indicator": investigation.get("indicator"),
        },
    )

    data = investigation.get(
        "hunt_data",
        investigation.get("events", []),
    )

    if not isinstance(hypothesis, dict):
        hypothesis = {
            "indicator": investigation.get("indicator"),
        }

    if not isinstance(data, list):
        data = [data]

    return engine.execute_hunt(
        hypothesis,
        data,
    )


def register_default_services(
    bridge: InvestigationServiceBridge,
) -> InvestigationServiceBridge:
    """
    Register Sentinel DNA's core intelligence engines.

    Existing engine instances are created once and retained by
    their runtime adapters.
    """

    if not isinstance(
        bridge,
        InvestigationServiceBridge,
    ):
        raise TypeError(
            "bridge must be an InvestigationServiceBridge."
        )

    risk_engine = RiskIntelligenceEngine()
    mitre_engine = MitreIntelligenceEngine()
    detection_engine = DetectionEngine()
    hunting_engine = HuntEngine()

    bridge.register_executor(
        name="risk_intelligence",
        capability="risk_assessment",
        executor=lambda investigation: _risk_executor(
            risk_engine,
            investigation,
        ),
    )

    bridge.register_executor(
        name="mitre_intelligence",
        capability="attack_mapping",
        executor=lambda investigation: _mitre_executor(
            mitre_engine,
            investigation,
        ),
    )

    bridge.register_executor(
        name="detection_engineering",
        capability="detection_analysis",
        executor=lambda investigation: _detection_executor(
            detection_engine,
            investigation,
        ),
    )

    bridge.register_executor(
        name="threat_hunting",
        capability="threat_hunting",
        executor=lambda investigation: _hunting_executor(
            hunting_engine,
            investigation,
        ),
    )

    return bridge


def create_default_service_bridge() -> InvestigationServiceBridge:
    """
    Create a fully configured Sentinel DNA service bridge.
    """

    bridge = InvestigationServiceBridge()

    return register_default_services(bridge)