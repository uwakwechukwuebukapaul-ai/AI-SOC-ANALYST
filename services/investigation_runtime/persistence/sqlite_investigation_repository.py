"""
SQLite investigation persistence.

Stores investigation state as JSON while keeping the
domain state model independent from SQLite.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from ..state import (
    InvestigationState,
    InvestigationStatus,
)

from .investigation_repository import (
    InvestigationRepository,
)


class SQLiteInvestigationRepository(
    InvestigationRepository
):
    """
    SQLite-backed investigation repository.

    The repository owns its database connection lifecycle
    and initializes its schema automatically.
    """

    def __init__(
        self,
        database_path: str | Path,
    ) -> None:
        self.database_path = Path(
            database_path
        )

        if (
            str(self.database_path)
            != ":memory:"
        ):
            self.database_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

        self._initialize()

    def _connect(
        self,
    ) -> sqlite3.Connection:
        connection = sqlite3.connect(
            str(self.database_path)
        )

        connection.row_factory = (
            sqlite3.Row
        )

        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS
                investigations (
                    investigation_id TEXT PRIMARY KEY,
                    investigation_json TEXT NOT NULL,
                    status TEXT NOT NULL,
                    intelligence_json TEXT NOT NULL,
                    correlation_json TEXT NOT NULL,
                    confidence_json TEXT NOT NULL,
                    finding_json TEXT NOT NULL,
                    errors_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    updated_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

    def create(
        self,
        state: InvestigationState,
    ) -> InvestigationState:
        if not isinstance(
            state,
            InvestigationState,
        ):
            raise TypeError(
                "State must be an InvestigationState."
            )

        if self.exists(
            state.investigation_id
        ):
            raise ValueError(
                f"Investigation "
                f"'{state.investigation_id}' "
                "already exists."
            )

        payload = state.to_dict()

        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO investigations (
                    investigation_id,
                    investigation_json,
                    status,
                    intelligence_json,
                    correlation_json,
                    confidence_json,
                    finding_json,
                    errors_json,
                    created_at,
                    started_at,
                    completed_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    payload["investigation_id"],
                    self._encode(
                        payload["investigation"]
                    ),
                    payload["status"],
                    self._encode(
                        payload["intelligence"]
                    ),
                    self._encode(
                        payload["correlation"]
                    ),
                    self._encode(
                        payload["confidence"]
                    ),
                    self._encode(
                        payload["finding"]
                    ),
                    self._encode(
                        payload["errors"]
                    ),
                    payload["created_at"],
                    payload["started_at"],
                    payload["completed_at"],
                    payload["updated_at"],
                ),
            )

            connection.commit()

        return state

    def get(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        if not investigation_id:
            raise ValueError(
                "Investigation ID is required."
            )

        with self._connect() as connection:
            row = connection.execute(
                """
                SELECT *
                FROM investigations
                WHERE investigation_id = ?
                """,
                (investigation_id,),
            ).fetchone()

        if row is None:
            raise KeyError(
                f"Investigation "
                f"'{investigation_id}' "
                "was not found."
            )

        return self._deserialize(row)

    def exists(
        self,
        investigation_id: str,
    ) -> bool:
        if not investigation_id:
            return False

        with self._connect() as connection:
            row = connection.execute(
                """
                SELECT 1
                FROM investigations
                WHERE investigation_id = ?
                LIMIT 1
                """,
                (investigation_id,),
            ).fetchone()

        return row is not None

    def update(
        self,
        state: InvestigationState,
    ) -> InvestigationState:
        if not isinstance(
            state,
            InvestigationState,
        ):
            raise TypeError(
                "State must be an InvestigationState."
            )

        if not self.exists(
            state.investigation_id
        ):
            raise KeyError(
                f"Investigation "
                f"'{state.investigation_id}' "
                "was not found."
            )

        payload = state.to_dict()

        with self._connect() as connection:
            connection.execute(
                """
                UPDATE investigations
                SET
                    investigation_json = ?,
                    status = ?,
                    intelligence_json = ?,
                    correlation_json = ?,
                    confidence_json = ?,
                    finding_json = ?,
                    errors_json = ?,
                    created_at = ?,
                    started_at = ?,
                    completed_at = ?,
                    updated_at = ?
                WHERE investigation_id = ?
                """,
                (
                    self._encode(
                        payload["investigation"]
                    ),
                    payload["status"],
                    self._encode(
                        payload["intelligence"]
                    ),
                    self._encode(
                        payload["correlation"]
                    ),
                    self._encode(
                        payload["confidence"]
                    ),
                    self._encode(
                        payload["finding"]
                    ),
                    self._encode(
                        payload["errors"]
                    ),
                    payload["created_at"],
                    payload["started_at"],
                    payload["completed_at"],
                    payload["updated_at"],
                    payload["investigation_id"],
                ),
            )

            connection.commit()

        return state

    def delete(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        state = self.get(
            investigation_id
        )

        with self._connect() as connection:
            connection.execute(
                """
                DELETE FROM investigations
                WHERE investigation_id = ?
                """,
                (investigation_id,),
            )

            connection.commit()

        return state

    def list(
        self,
    ) -> list[InvestigationState]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT *
                FROM investigations
                ORDER BY created_at ASC
                """
            ).fetchall()

        return [
            self._deserialize(row)
            for row in rows
        ]

    @staticmethod
    def _encode(
        value: Any,
    ) -> str:
        return json.dumps(
            value,
            separators=(",", ":"),
        )

    @staticmethod
    def _decode(
        value: str,
    ) -> Any:
        return json.loads(value)

    @classmethod
    def _deserialize(
        cls,
        row: sqlite3.Row,
    ) -> InvestigationState:
        state = InvestigationState(
            investigation_id=row[
                "investigation_id"
            ],
            investigation=cls._decode(
                row["investigation_json"]
            ),
            status=InvestigationStatus(
                row["status"]
            ),
            intelligence=cls._decode(
                row["intelligence_json"]
            ),
            correlation=cls._decode(
                row["correlation_json"]
            ),
            confidence=cls._decode(
                row["confidence_json"]
            ),
            finding=cls._decode(
                row["finding_json"]
            ),
            errors=cls._decode(
                row["errors_json"]
            ),
            created_at=datetime.fromisoformat(
                row["created_at"]
            ),
            started_at=(
                datetime.fromisoformat(
                    row["started_at"]
                )
                if row["started_at"]
                else None
            ),
            completed_at=(
                datetime.fromisoformat(
                    row["completed_at"]
                )
                if row["completed_at"]
                else None
            ),
            updated_at=datetime.fromisoformat(
                row["updated_at"]
            ),
        )

        return state