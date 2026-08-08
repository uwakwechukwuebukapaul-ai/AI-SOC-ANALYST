"""
Sentinel DNA Investigation Coordinator

Enterprise investigation orchestration boundary.

Coordinates:

Execution Plan
|
Agent Pipeline
|
Runtime
|
Persistence
"""

from __future__ import annotations

from typing import Any


from services.intelligence.orchestration.agent_pipeline import (
    AgentPipeline,
)

from services.intelligence.orchestration.orchestration_result import (
    OrchestrationResult,
)

from services.intelligence.storage.investigation_repository import (
    InvestigationRepository,
)


class InvestigationCoordinator:
    """
    Coordinates autonomous investigations.
    """

    def __init__(
        self,
        registry: Any,
        runtime: Any,
        pipeline: AgentPipeline | None = None,
        repository: InvestigationRepository | None = None,
    ) -> None:

        self.pipeline = (
            pipeline
            or AgentPipeline(
                registry=registry,
                runtime=runtime,
            )
        )

        self.repository = (
            repository
            or InvestigationRepository()
        )


    # ----------------------------------------------------------
    # Investigation execution
    # ----------------------------------------------------------

    def investigate(
        self,
        case_id: str,
        alert: dict[str, Any],
    ) -> OrchestrationResult:
        """
        Execute investigation lifecycle.
        """

        self.repository.create(
            case_id=case_id,
            alert=alert,
        )


        context = self._create_context(
            case_id,
            alert,
        )


        plan = self._create_plan()


        result = self.pipeline.execute(
            plan=plan,
            context=context,
        )


        if result.success:

            self.repository.update_status(
                case_id,
                "completed",
            )

        else:

            self.repository.update_status(
                case_id,
                "failed",
            )


        return result



    # ----------------------------------------------------------
    # Context
    # ----------------------------------------------------------

    def _create_context(
        self,
        case_id: str,
        alert: dict[str, Any],
    ):

        from services.intelligence.orchestration.orchestration_context import (
            OrchestrationContext,
        )


        return OrchestrationContext(
            case_id=case_id,
            alert=alert,
        )



    # ----------------------------------------------------------
    # Plan
    # ----------------------------------------------------------

    def _create_plan(self):

        from services.intelligence.orchestration.investigation_plans import (
            InvestigationPlans,
        )


        return InvestigationPlans.standard_investigation()