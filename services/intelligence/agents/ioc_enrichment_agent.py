"""
IOC Enrichment Agent

First investigation agent in the Sentinel DNA pipeline.
"""

from __future__ import annotations

from services.intelligence.agents.base_agent import BaseAgent
from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_metadata import AgentMetadata
from services.intelligence.agents.agent_capability import AgentCapability
from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)

from .ioc_enricher import IOCEnricher


class IOCEnrichmentAgent(BaseAgent):

    def __init__(self):

        self._metadata = AgentMetadata(
            name="IOC Enrichment Agent",
            version="1.0",
            description="Enriches Indicators of Compromise.",
            capabilities=[
                "ioc_enrichment",
                "reputation_lookup",
            ],
            tags=[
                "ioc",
                "threat_intelligence",
            ],
        )

        self._capabilities = [
            AgentCapability(
                name="ioc_enrichment",
                description="Offline IOC enrichment",
                inputs=["ioc"],
                outputs=["enrichment"],
            ),
            AgentCapability(
                name="reputation_lookup",
                description="IOC reputation lookup",
                inputs=["ioc"],
                outputs=["reputation"],
            ),
        ]

    @property
    def metadata(self) -> AgentMetadata:
        return self._metadata

    @property
    def capabilities(self) -> list[AgentCapability]:
        return self._capabilities

    def validate(
        self,
        context: AgentContext,
    ) -> bool:

        return context is not None

    def execute(
        self,
        context: AgentContext,
    ) -> AgentResult:

        if not self.validate(context):

            return AgentResult(
                agent_name=self.metadata.name,
                status=AgentExecutionStatus.FAILED,
                confidence=0.0,
                errors=[
                    "Invalid investigation context.",
                ],
            )

        result = AgentResult(
            agent_name=self.metadata.name,
            status=AgentExecutionStatus.SUCCESS,
            confidence=100.0,
        )

        indicators = []

        indicators.extend(context.iocs)

        if "iocs" in context.shared_data:
            indicators.extend(context.shared_data["iocs"])

        seen = set()

        for indicator in indicators:

            if indicator in seen:
                continue

            seen.add(indicator)

            enrichment = IOCEnricher.enrich(indicator)

            result.add_finding(
                enrichment.to_dict()
            )

        result.metadata["ioc_count"] = len(result.findings)
        result.metadata["engine"] = "offline"

        result.add_artifact(
            "ioc_enrichment",
            result.findings,
        )

        return result

    def summarize(
        self,
        result: AgentResult,
    ) -> str:

        return (
            f"IOC Enrichment completed. "
            f"{len(result.findings)} indicators enriched."
        )

    def cleanup(self) -> None:
        pass