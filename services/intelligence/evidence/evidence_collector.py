"""
Sentinel DNA Evidence Collector

Collects artifacts from investigations.
"""

from __future__ import annotations

from typing import Any

from services.intelligence.evidence.artifact import (
    Artifact,
)


class EvidenceCollector:
    """
    Evidence ingestion service.
    """

    def __init__(self):

        self.artifacts: list[Artifact] = []


    def collect(
        self,
        artifact: Artifact,
    ) -> Artifact:

        self.artifacts.append(
            artifact
        )

        return artifact



    def collect_from_alert(
        self,
        alert: dict[str, Any],
    ) -> list[Artifact]:

        results = []


        if alert.get("indicator"):

            artifact = Artifact(
                artifact_id="ioc-001",
                artifact_type="ioc",
                value=alert["indicator"],
                source="alert",
            )

            self.collect(
                artifact
            )

            results.append(
                artifact
            )


        return results



    def all(self):

        return self.artifacts