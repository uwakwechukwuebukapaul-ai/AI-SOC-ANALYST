from services.intelligence.orchestration.execution_plan import (
    ExecutionPlan,
)


class InvestigationPlans:
    """
    Standard investigation workflow definitions.
    """

    @staticmethod
    def standard_investigation():
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