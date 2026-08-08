"""
Sentinel DNA Investigation Repository

Persistence boundary for investigation lifecycle data.

Responsibilities:
- create investigations
- retrieve investigations
- update investigation status
- maintain investigation metadata

Future adapters:
- SQLite
- PostgreSQL
- Elasticsearch
- OpenSearch
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class InvestigationRepository:
    """
    Investigation persistence repository.

    Current:
        In-memory implementation.

    Future:
        Database-backed repository.
    """

    def __init__(self) -> None:
        self._investigations: dict[
            str,
            dict[str, Any],
        ] = {}


    def create(
        self,
        case_id: str,
        alert: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create investigation record.
        """

        investigation = {
            "case_id": case_id,
            "alert": alert,
            "status": "created",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        self._investigations[case_id] = investigation

        return investigation


    def get(
        self,
        case_id: str,
    ) -> dict[str, Any] | None:
        """
        Retrieve investigation.
        """

        return self._investigations.get(
            case_id
        )


    def update_status(
        self,
        case_id: str,
        status: str,
    ) -> dict[str, Any] | None:
        """
        Update lifecycle state.
        """

        investigation = self.get(
            case_id
        )

        if investigation is None:
            return None


        investigation["status"] = status

        investigation["updated_at"] = (
            datetime.now(
                timezone.utc
            ).isoformat()
        )

        return investigation


    def delete(
        self,
        case_id: str,
    ) -> bool:
        """
        Delete investigation.
        """

        if case_id not in self._investigations:
            return False


        del self._investigations[case_id]

        return True


    def exists(
        self,
        case_id: str,
    ) -> bool:
        """
        Check investigation existence.
        """

        return case_id in self._investigations


    def list_all(self) -> list[dict[str, Any]]:
        """
        Return all investigations.
        """

        return list(
            self._investigations.values()
        )