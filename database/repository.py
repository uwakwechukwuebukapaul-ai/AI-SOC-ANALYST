"""
Sentinel DNA
Database Repository Layer

Handles all database operations for incidents.
"""

import json

from database.connection import database
from database.models import Incident


class IncidentRepository:
    """
    Repository responsible for Incident database operations.
    """

    def create(self, incident: Incident) -> int:
        """
        Save a new incident.
        """

        incident.validate()

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO incidents
                (
                    time,
                    threat,
                    severity,
                    risk_score,
                    mitre,
                    response_status,
                    status,
                    evidence,
                    actions,
                    analyst,
                    notes
                )

                VALUES
                (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    incident.timestamp,
                    incident.threat,
                    incident.severity,
                    incident.risk_score,
                    incident.mitre,
                    incident.response_status,
                    incident.status,
                    incident.evidence,
                    json.dumps(incident.actions),
                    incident.analyst,
                    incident.notes,
                ),
            )

            return cursor.lastrowid


    def get_all(self) -> list[Incident]:
        """
        Return all incidents.
        """

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM incidents
                ORDER BY id DESC
                """
            )

            rows = cursor.fetchall()


            return [
                self._convert(row)
                for row in rows
            ]


    def get_by_id(self, incident_id: int):
        """
        Get single incident.
        """

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM incidents
                WHERE id=?
                """,
                (incident_id,),
            )

            row = cursor.fetchone()


            if row:

                return self._convert(row)

            return None


    def update_status(
        self,
        incident_id: int,
        status: str
    ):
        """
        Update incident status.
        """

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE incidents

                SET status=?

                WHERE id=?
                """,
                (
                    status,
                    incident_id
                )
            )


    def assign_analyst(
        self,
        incident_id: int,
        analyst: str
    ):
        """
        Assign analyst.
        """

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE incidents

                SET analyst=?

                WHERE id=?
                """,
                (
                    analyst,
                    incident_id
                )
            )


    def add_notes(
        self,
        incident_id: int,
        notes: str
    ):
        """
        Add investigation notes.
        """

        with database.session() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE incidents

                SET notes=?

                WHERE id=?
                """,
                (
                    notes,
                    incident_id
                )
            )


    def _convert(self, row):
        """
        Convert SQLite row into Incident object.
        """

        data = dict(row)

        try:

            data["actions"] = json.loads(
                data.get("actions", "[]")
            )

        except:

            data["actions"] = []


        return Incident.from_dict(data)


incident_repository = IncidentRepository()