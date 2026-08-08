"""
Sentinel DNA Investigation Intelligence

Combines:

Artifacts
+
Correlation
+
Reasoning

into autonomous investigation intelligence.
"""

from __future__ import annotations

from typing import Any


from services.intelligence.correlation.correlation_engine import (
    CorrelationEngine,
)


from services.intelligence.reasoning.reasoning_engine import (
    ReasoningEngine,
)



class InvestigationIntelligence:
    """
    AI investigation intelligence coordinator.
    """

    def __init__(
        self,
        correlation_engine: CorrelationEngine | None = None,
        reasoning_engine: ReasoningEngine | None = None,
    ) -> None:


        self.correlation_engine = (
            correlation_engine
            or CorrelationEngine()
        )


        self.reasoning_engine = (
            reasoning_engine
            or ReasoningEngine()
        )



    # --------------------------------------------------
    # Analyze investigation evidence
    # --------------------------------------------------

    def analyze(
        self,
        artifacts: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Execute intelligence pipeline.
        """


        correlation = (
            self.correlation_engine.correlate(
                artifacts
            )
        )


        reasoning = (
            self.reasoning_engine.analyze(
                correlation["findings"]
            )
        )


        return {

            "correlation":
                correlation,

            "reasoning":
                reasoning,

            "status":
                "completed",
        }