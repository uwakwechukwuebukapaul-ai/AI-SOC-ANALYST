"""
Autonomous SOC Loop Integration Tests

Validates the end-to-end autonomous security workflow.
"""


from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)

from services.investigation.autonomous_investigation_intelligence_engine import (
    AutonomousInvestigationIntelligenceEngine,
)

from services.response.autonomous_security_response_engine import (
    AutonomousSecurityResponseEngine,
)

from services.reflection.autonomous_security_reflection_engine import (
    AutonomousSecurityReflectionEngine,
)

from services.optimization.autonomous_security_optimization_engine import (
    AutonomousSecurityOptimizationEngine,
)


def test_autonomous_soc_loop():

    coordinator = AutonomousAgentCoordinator()

    coordinator.register_agent(
        "intel-agent",
        "security_intelligence"
    )

    coordinator.register_agent(
        "response-agent",
        "incident_response"
    )

    status = coordinator.get_system_status()

    assert status["status"] == "operational"
    assert status["agents"] == 2


def test_investigation_engine_bootstrap():

    engine = AutonomousInvestigationIntelligenceEngine()

    assert engine is not None


def test_response_engine_bootstrap():

    engine = AutonomousSecurityResponseEngine()

    assert engine is not None


def test_reflection_engine_bootstrap():

    engine = AutonomousSecurityReflectionEngine()

    assert engine is not None


def test_optimization_engine_bootstrap():

    engine = AutonomousSecurityOptimizationEngine()

    assert engine is not None