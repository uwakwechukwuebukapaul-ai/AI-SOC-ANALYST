"""
Sentinel DNA MITRE Mapper

Maps investigation evidence
to ATT&CK techniques.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.mitre.mitre_database import (
    MitreDatabase,
)


class MitreMapper:


    def __init__(
        self,
        database=None,
    ):

        self.database = (
            database
            or MitreDatabase()
        )



    def map_artifact(
        self,
        artifact: dict[str, Any],
    ):


        mappings = []


        artifact_type = artifact.get(
            "type"
        )


        if artifact_type == "email":

            technique = self.database.get(
                "T1566"
            )

            mappings.append(
                technique
            )


        if artifact_type == "file":

            technique = self.database.get(
                "T1204"
            )

            mappings.append(
                technique
            )


        return [

            item.to_dict()

            for item in mappings

            if item
        ]



    def map_findings(
        self,
        findings: list[dict[str, Any]],
    ):


        results = []


        for finding in findings:

            results.extend(
                self.map_artifact(
                    finding
                )
            )


        return results