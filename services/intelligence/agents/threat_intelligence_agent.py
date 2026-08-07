"""
Threat Intelligence Agent

Second investigation agent in the Sentinel DNA pipeline.

Responsibilities

- Reads Indicators of Compromise (IOCs)
- Enriches every IOC
- Performs threat assessment
- Produces standardized AgentResult output

Future integrations

- VirusTotal
- AbuseIPDB
- MISP
- AlienVault OTX
- URLHaus
- Internal Threat Intelligence
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
from .threat_intelligence_engine import ThreatIntelligenceEngine


class ThreatIntelligenceAgent(BaseAgent):

    def __init__(self):

        self._metadata = AgentMetadata(
            name="Threat Intelligence Agent",
            version="1.0",
            description="Performs enterprise threat intelligence analysis.",
            capabilities=[
                "threat_intelligence",
                "threat_assessment",
            ],
            tags=[
                "threat",
                "intelligence",
                "ioc",
            ],
        )

        self._capabilities = [
            AgentCapability(
                name="threat_intelligence",
                description="Threat intelligence assessment",
                inputs=["ioc"],
                outputs=["assessment"],
            ),
            AgentCapability(
                name="threat_assessment",
                description="Threat scoring",
                inputs=["enrichment"],
                outputs=["threat_level"],
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
            indicators.extend(
                context.shared_data["iocs"]
            )

        seen = set()

        assessments = []

        for indicator in indicators:

            if indicator in seen:
                continue

            seen.add(indicator)

            enrichment = IOCEnricher.enrich(
                indicator
            )

            assessment = (
                ThreatIntelligenceEngine.assess(
                    enrichment
                )
            )

            assessments.append(assessment)

            result.add_finding(
                assessment.to_dict()
            )

        result.metadata["assessment_count"] = len(
            assessments
        )

        result.metadata["overall_threat"] = (
            ThreatIntelligenceEngine
            .overall_level(assessments)
            .value
        )

        result.metadata["average_confidence"] = (
            ThreatIntelligenceEngine
            .average_confidence(assessments)
        )

        result.metadata["total_score"] = (
            ThreatIntelligenceEngine
            .total_score(assessments)
        )

        result.add_artifact(
            "threat_assessments",
            result.findings,
        )

        return result

    def summarize(
        self,
        result: AgentResult,
    ) -> str:

        return (
            f"Threat Intelligence completed. "
            f"{len(result.findings)} indicators assessed. "
            f"Overall threat: "
            f"{result.metadata['overall_threat']}."
        )

    def cleanup(self) -> None:
        pass