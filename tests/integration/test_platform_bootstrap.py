"""
Sentinel DNA Platform Bootstrap Integration Test
"""

from services.platform.autonomous_agent_coordinator import (
    AutonomousAgentCoordinator,
)


def test_platform_bootstrap():

    coordinator = AutonomousAgentCoordinator()

    assert coordinator is not None

    status = coordinator.get_system_status()

    assert status is not None