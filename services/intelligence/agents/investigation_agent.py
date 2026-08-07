"""
Sentinel DNA Investigation Agent

Enterprise investigation planning agent.
"""

from __future__ import annotations

from services.intelligence.agents.base_agent import BaseAgent
from services.intelligence.agents.agent_capability import AgentCapability
from services.intelligence.agents.agent_context import AgentContext
from services.intelligence.agents.agent_metadata import AgentMetadata
from services.intelligence.agents.agent_result import (
    AgentExecutionStatus,
    AgentResult,
)


class InvestigationAgent(BaseAgent):
    """
    Primary investigation planning agent.
    """

    @property
    def metadata(self) -> AgentMetadata:

        return AgentMetadata(
            name="Investigation Agent",
            version="1.0",
            description="Plans AI investigations.",
            investigation_types=[
                "phishing",
                "malware",
                "credential_access",
                "lateral_movement",
            ],
            tags=[
                "investigation",
                "planner",
            ],
        )

    @property
    def capabilities(self) -> list[AgentCapability]:

        return [
            AgentCapability(
                name="investigation_planning",
                description="Creates investigation plans",
                category="planning",
            )
        ]

    def validate(
        self,
        context: AgentContext,
    ) -> bool:

        return bool(context.case_id)

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
                    "Invalid investigation context."
                ],
            )

        plan = [
            "IOC Enrichment",
            "Threat Intelligence",
            "MITRE Mapping",
            "Timeline Analysis",
            "Risk Scoring",
            "Recommendations",
            "Final Report",
        ]

        result = AgentResult(
            agent_name=self.metadata.name,
            status=AgentExecutionStatus.SUCCESS,
            confidence=100.0,
        )

        result.artifacts["investigation_plan"] = plan

        result.metrics["steps"] = len(plan)

        return result

    def summarize(
        self,
        result: AgentResult,
    ) -> str:

        return (
            f"Investigation plan created with "
            f"{result.metrics['steps']} steps."
        )

    def cleanup(
        self,
    ) -> None:
        pass