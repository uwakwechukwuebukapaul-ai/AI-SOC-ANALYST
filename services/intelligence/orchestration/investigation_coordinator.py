"""
Sentinel DNA Investigation Coordinator

Coordinates complete intelligence investigations.

Responsibilities
----------------
- create investigation context
- select investigation plan
- invoke AgentPipeline
- return OrchestrationResult

Non-responsibilities
--------------------
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

    The coordinator owns workflow selection and context creation.

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

        Returns
        -------
        OrchestrationResult
            Aggregated result of the investigation plan.
        """

        context = OrchestrationContext(
            case_id=case_id,
            alert=alert,
        )

        plan = InvestigationPlans.standard_investigation()

        result = self.pipeline.execute(
            plan=plan,
            context=context,
        )

        return result