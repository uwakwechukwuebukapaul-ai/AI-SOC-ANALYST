"""
Sentinel DNA Investigation Coordinator

Coordinates complete intelligence investigations.

## Responsibilities

- create investigation context
- select investigation plan
- invoke AgentPipeline
- synchronize orchestration results into investigation context
- return OrchestrationResult

## Non-responsibilities

- agent execution
- scheduling
- worker management
- runtime lifecycle
- retries
- runtime metrics
- resource allocation
- policy enforcement

The runtime is injected into the orchestration layer and remains
the canonical execution boundary.
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
    Coordinates a complete Sentinel DNA investigation workflow.

    The coordinator owns workflow selection, investigation context
    creation, and aggregation of pipeline output.

    Agent execution is delegated to AgentPipeline.

    Runtime execution is delegated further through AgentPipeline
    into the canonical Sentinel DNA runtime.
    """

    def __init__(
        self,
        registry: Any,
        runtime: Any | None = None,
    ) -> None:
        """
        Initialize the investigation coordinator.

        Parameters
        ----------
        registry:
            Compatibility agent registry used for agent resolution.

        runtime:
            Optional canonical intelligence runtime.

            When supplied, AgentPipeline routes agent execution
            through the runtime.

            When omitted, AgentPipeline retains its legacy
            registry execution path for compatibility.
        """

        self.registry = registry
        self.runtime = runtime

        self.pipeline = AgentPipeline(
            registry=registry,
            runtime=runtime,
        )

    # ------------------------------------------------------------------
    # Investigation
    # ------------------------------------------------------------------

    def investigate(
        self,
        case_id: str,
        alert: dict[str, Any],
    ) -> OrchestrationResult:
        """
        Execute the standard Sentinel DNA investigation workflow.

        The coordinator creates the investigation context, selects
        the canonical investigation plan, executes the plan through
        AgentPipeline, and synchronizes successful agent results back
        into the investigation context.

        Returns
        -------
        OrchestrationResult
            Aggregated result of the investigation plan.
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
            context=context,
            result=result,
        )

        return result

    # ------------------------------------------------------------------
    # Context creation
    # ------------------------------------------------------------------

    @staticmethod
    def _create_context(
        case_id: str,
        alert: dict[str, Any],
    ) -> OrchestrationContext:
        """
        Create the investigation-level orchestration context.
        """

        if not case_id or not case_id.strip():
            raise ValueError(
                "Case ID is required."
            )

        if not isinstance(alert, dict):
            raise TypeError(
                "Alert must be a dictionary."
            )

        return OrchestrationContext(
            case_id=case_id,
            alert=dict(alert),
        )

    # ------------------------------------------------------------------
    # Result synchronization
    # ------------------------------------------------------------------

    @staticmethod
    def _synchronize_results(
        context: OrchestrationContext,
        result: OrchestrationResult,
    ) -> None:
        """
        Synchronize successful pipeline results into the
        investigation context.

        OrchestrationResult remains the execution outcome.

        OrchestrationContext remains the investigation state.

        This method deliberately does not copy orchestration errors
        into context state because errors belong to the execution
        result boundary.
        """

        for agent_name, agent_result in result.results.items():
            context.add_result(
                agent_name=agent_name,
                result=agent_result,
            )