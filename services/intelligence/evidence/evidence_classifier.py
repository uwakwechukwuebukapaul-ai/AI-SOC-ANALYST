"""
Sentinel DNA Evidence Classifier

Determines artifact categories.
"""

from __future__ import annotations

from services.intelligence.evidence.artifact import (
    Artifact,
)


class EvidenceClassifier:
    """
    Classifies investigation evidence.
    """


    def classify(
        self,
        artifact: Artifact,
    ) -> str:


        value = str(
            artifact.value
        ).lower()


        if "." in value:

            artifact.metadata[
                "classification"
            ] = "domain"


            return "domain"


        if value.count(".") == 3:

            artifact.metadata[
                "classification"
            ] = "ip"


            return "ip"


        artifact.metadata[
            "classification"
        ] = "unknown"


        return "unknown"