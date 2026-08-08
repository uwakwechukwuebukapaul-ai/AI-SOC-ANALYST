"""
Sentinel DNA Investigation Plans

Canonical investigation workflow definitions.

Investigation plans describe WHAT should execute.

The runtime framework determines HOW execution occurs.
"""

from __future__ import annotations

from services.intelligence.orchestration.execution_plan import (
    ExecutionPlan,
)


class InvestigationPlans:
    """
    Standard Sentinel DNA investigation workflow definitions.
    """

    @staticmethod
    def standard_investigation() -> ExecutionPlan:
        """
        Return the standard security investigation plan.

        Current AI Investigator v1 workflow:

        Investigation Agent
            |
            v
        IOC Enrichment Agent
            |
            v
        Threat Intelligence Agent

        Additional agents such as MITRE, Risk,
        Recommendation, Timeline and Report will be
        introduced as their implementations mature.
        """

        return ExecutionPlan(
            name="Standard Security Investigation",
            agents=[
                "Investigation Agent",
                "IOC Enrichment Agent",
                "Threat Intelligence Agent",
            ],
            metadata={
                "workflow": "ai_investigator_v1",
                "version": "1.0",
                "execution_mode": "runtime",
            },
        )