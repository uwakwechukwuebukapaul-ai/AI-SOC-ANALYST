"""
Sentinel DNA Investigation Coordinator

Coordinates complete intelligence investigations.

Responsibilities:

- create investigation context
- select investigation plan
- invoke AgentPipeline
- synchronize orchestration results into investigation context
- return OrchestrationResult

Runtime remains the execution boundary.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.orchestration.agent_pipeline import (
    AgentPipeline,
)

from services.intelligence.orchestration.investigation_plans import (
    InvestigationPlans,
)

from services.intelligence.orchestration.orchestration_context import (
    OrchestrationContext,
)

from services.intelligence.orchestration.orchestration_result import (
    OrchestrationResult,
)


class InvestigationCoordinator:
    """
    Coordinates Sentinel DNA investigations.
    """

    def __init__(
        self,
        registry: Any,
        runtime: Any | None = None,
    ) -> None:

        self.registry = registry
        self.runtime = runtime

        self.pipeline = AgentPipeline(
            registry=registry,
            runtime=runtime,
        )

    # --------------------------------------------------------------
    # Investigation
    # --------------------------------------------------------------

    def investigate(
        self,
        case_id: str,
        alert: dict[str, Any],
    ) -> OrchestrationResult:
        """
        Execute investigation workflow.
        """

        context = self._create_context(
            case_id=case_id,
            alert=alert,
        )

        plan = InvestigationPlans.standard_investigation()

        result = self.pipeline.execute(
            plan=plan,
            context=context,
        )

        self._synchronize_results(
            context,
            result,
        )

        return result


    # --------------------------------------------------------------
    # Context
    # --------------------------------------------------------------

    @staticmethod
    def _create_context(
        case_id: str,
        alert: dict[str, Any],
    ) -> OrchestrationContext:

        if not case_id:
            raise ValueError(
                "Case ID required."
            )

        if not isinstance(alert, dict):
            raise TypeError(
                "Alert must be dictionary."
            )

        return OrchestrationContext(
            case_id=case_id,
            alert=dict(alert),
        )


    # --------------------------------------------------------------
    # Synchronization
    # --------------------------------------------------------------

    @staticmethod
    def _synchronize_results(
        context: OrchestrationContext,
        result: OrchestrationResult,
    ) -> None:

        for agent_name, agent_result in result.results.items():

            context.add_result(
                agent_name=agent_name,
                result=agent_result,
            )