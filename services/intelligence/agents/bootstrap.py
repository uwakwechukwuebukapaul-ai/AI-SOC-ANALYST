"""
Sentinel DNA Agent Bootstrap

Central initialization point for intelligence agents.

Responsibilities:

- create intelligence agents
- register agents for orchestration
- register agents into runtime lifecycle
- connect agent capabilities to runtime execution
"""

from __future__ import annotations

from services.intelligence.agents.agent_registry import (
    AgentRegistry,
)

from services.intelligence.agents.investigation_agent import (
    InvestigationAgent,
)

from services.intelligence.agents.ioc_enrichment_agent import (
    IOCEnrichmentAgent,
)

from services.intelligence.agents.threat_intelligence_agent import (
    ThreatIntelligenceAgent,
)


def create_agents() -> list:
    """
    Create Sentinel DNA intelligence agents.
    """

    return [
        InvestigationAgent(),
        IOCEnrichmentAgent(),
        ThreatIntelligenceAgent(),
    ]


def register_agents(
    registry: AgentRegistry,
) -> list:
    """
    Register agents into orchestration registry.

    Returns created agents for optional
    runtime registration.
    """

    agents = create_agents()

    for agent in agents:
        registry.register(agent)

    return agents


def bootstrap_agents(
    registry: AgentRegistry,
    lifecycle_service=None,
    runtime_adapter=None,
) -> list:
    """
    Enterprise agent bootstrap.

    Initializes:

    Agent Registry
        |
        v
    Runtime Lifecycle
        |
        v
    Runtime Capability Adapter
    """

    agents = register_agents(
        registry
    )

    for agent in agents:

        if lifecycle_service is not None:
            lifecycle_service.register(
                agent
            )

        if runtime_adapter is not None:
            runtime_adapter.register_agent(
                agent
            )

    return agents