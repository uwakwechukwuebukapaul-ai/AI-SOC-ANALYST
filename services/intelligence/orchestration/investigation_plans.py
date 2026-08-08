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
        """

        return ExecutionPlan(
            name="Standard Security Investigation",
            agents=[
                "IOC Agent",
                "Threat Intelligence Agent",
                "MITRE Agent",
                "Timeline Agent",
                "Risk Agent",
                "Recommendation Agent",
                "Report Agent",
            ],
        )