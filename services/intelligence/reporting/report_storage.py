"""
Sentinel DNA Report Storage

Application storage adapter for investigation reports.

Responsibilities:

- coordinate report persistence
- hide repository implementation
- provide stable storage interface

Non-responsibilities:

- report generation
- orchestration
- API handling
"""

from __future__ import annotations

from typing import Any

from services.intelligence.storage.report_repository import (
    ReportRepository,
)


class ReportStorage:
    """
    Investigation report storage service.
    """

    def __init__(
        self,
        repository: ReportRepository | None = None,
    ) -> None:

        self.repository = (
            repository
            or ReportRepository()
        )


    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save_report(
        self,
        case_id: str,
        report: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Persist investigation report.
        """

        return self.repository.save(
            case_id=case_id,
            report=report,
        )


    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------

    def get_report(
        self,
        case_id: str,
    ) -> dict[str, Any] | None:
        """
        Retrieve investigation report.
        """

        return self.repository.get(
            case_id
        )


    # --------------------------------------------------
    # Exists
    # --------------------------------------------------

    def exists(
        self,
        case_id: str,
    ) -> bool:
        """
        Check report existence.
        """

        return self.repository.exists(
            case_id
        )


    # --------------------------------------------------
    # List
    # --------------------------------------------------

    def list_reports(self) -> list[dict[str, Any]]:
        """
        Return all reports.
        """

        return self.repository.list_all()