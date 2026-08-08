"""
Sentinel DNA Report Service

Application service layer for investigation reporting.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.reporting.report_builder import (
    ReportBuilder,
)

from services.intelligence.reporting.investigation_report import (
    InvestigationReport,
)


class ReportService:
    """
    Sentinel DNA Investigation Report Service.
    """

    def __init__(
        self,
        builder: ReportBuilder | None = None,
    ) -> None:

        self.builder = (
            builder
            or ReportBuilder()
        )

        # Temporary v1 storage.
        # Replace with repository layer later.
        self._reports: dict[
            str,
            InvestigationReport
        ] = {}


    # --------------------------------------------------
    # Generate
    # --------------------------------------------------

    def generate_report(
        self,
        case_id: str,
        orchestration_result: Any,
    ) -> InvestigationReport:

        if not case_id:
            raise ValueError(
                "Case ID is required."
            )

        if orchestration_result is None:
            raise ValueError(
                "Orchestration result is required."
            )


        report = self.builder.build(
            case_id=case_id,
            orchestration_result=orchestration_result,
        )


        self._reports[
            case_id
        ] = report


        return report



    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def get_report(
        self,
        case_id: str,
    ) -> InvestigationReport | None:
        """
        Retrieve existing investigation report.
        """

        return self._reports.get(
            case_id
        )



    # --------------------------------------------------
    # Serialization
    # --------------------------------------------------

    def serialize_report(
        self,
        report: InvestigationReport,
    ) -> dict[str, Any]:

        return {
            "case_id": report.case_id,
            "severity": report.severity,
            "risk_score": report.risk_score,
            "findings": report.findings,
            "recommendations": report.recommendations,
            "confidence": getattr(
                report,
                "confidence",
                None,
            ),
            "agent_results": getattr(
                report,
                "agent_results",
                {},
            ),
            "metadata": getattr(
                report,
                "metadata",
                {},
            ),
        }



    # --------------------------------------------------
    # API helper
    # --------------------------------------------------

    def build_response(
        self,
        case_id: str,
        orchestration_result: Any,
    ) -> dict[str, Any]:

        report = self.generate_report(
            case_id,
            orchestration_result,
        )

        return self.serialize_report(
            report
        )