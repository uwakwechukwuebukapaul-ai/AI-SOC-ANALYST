"""
Sentinel DNA Report Enrichment Engine

Adds AI intelligence context
to investigation reports.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.reporting.intelligence.attack_story_builder import (
    AttackStoryBuilder,
)

from services.intelligence.reporting.intelligence.analyst_summary_generator import (
    AnalystSummaryGenerator,
)



class ReportEnrichment:
    """
    Enhances investigation reports.
    """

    def __init__(
        self,
        story_builder=None,
        summary_generator=None,
    ):


        self.story_builder = (
            story_builder
            or AttackStoryBuilder()
        )


        self.summary_generator = (
            summary_generator
            or AnalystSummaryGenerator()
        )



    def enrich(
        self,
        report: dict[str, Any],
        intelligence: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Add intelligence fields.
        """

        report = dict(
            report
        )


        report[
            "attack_story"
        ] = self.story_builder.build(
            intelligence.get(
                "reasoning",
                {},
            )
        )


        report[
            "analyst_summary"
        ] = self.summary_generator.generate(
            intelligence
        )


        report[
            "intelligence_status"
        ] = "completed"


        return report