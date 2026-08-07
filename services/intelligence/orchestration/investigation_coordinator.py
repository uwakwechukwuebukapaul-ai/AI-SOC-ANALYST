from services.intelligence.orchestration.agent_pipeline import AgentPipeline
from services.intelligence.orchestration.investigation_plans import InvestigationPlans
from services.intelligence.orchestration.orchestration_context import (
    OrchestrationContext,
)


class InvestigationCoordinator:
    """
    Coordinates a complete Sentinel DNA investigation workflow.
    """

    def __init__(self, registry):
        self.registry = registry
        self.pipeline = AgentPipeline(registry)

    def investigate(self, case_id: str, alert: dict):
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