"""
Sentinel DNA Intelligent Report Service

Enterprise reporting orchestration layer.

Combines:

- Investigation Report
- Evidence Intelligence
- Correlation
- AI Reasoning
- Analyst Summary
"""

from __future__ import annotations

from typing import Any


from services.intelligence.reporting.report_service import (
    ReportService,
)


from services.intelligence.reporting.intelligence.report_enrichment import (
    ReportEnrichment,
)


from services.intelligence.investigation.investigation_intelligence import (
    InvestigationIntelligence,
)



class IntelligentReportService:
    """
    Generates enriched AI investigation reports.
    """



    def __init__(
        self,
        report_service: ReportService | None = None,
        intelligence: InvestigationIntelligence | None = None,
        enrichment: ReportEnrichment | None = None,
    ) -> None:


        self.report_service = (
            report_service
            or ReportService()
        )


        self.intelligence = (
            intelligence
            or InvestigationIntelligence()
        )


        self.enrichment = (
            enrichment
            or ReportEnrichment()
        )



    # --------------------------------------------------
    # Generate intelligent report
    # --------------------------------------------------

    def generate(
        self,
        case_id: str,
        orchestration_result: Any,
        artifacts: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Create final AI investigation report.
        """


        report = (
            self.report_service.build_response(
                case_id=case_id,
                orchestration_result=orchestration_result,
            )
        )


        intelligence = (
            self.intelligence.analyze(
                artifacts
            )
        )


        enriched_report = (
            self.enrichment.enrich(
                report,
                intelligence,
            )
        )


        enriched_report[
            "intelligence"
        ] = intelligence


        return enriched_report