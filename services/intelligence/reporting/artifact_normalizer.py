"""
Sentinel DNA Artifact Normalizer

Converts raw investigation input into
correlation-safe intelligence artifacts.

Responsibilities:

- normalize IOC data
- remove non-hashable objects
- prepare evidence for correlation
"""


from __future__ import annotations

from typing import Any



class ArtifactNormalizer:
    """
    Normalizes investigation artifacts.
    """



    def normalize(
        self,
        alert: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """
        Convert alert payload into
        correlation-compatible artifacts.
        """


        artifacts: list[dict[str, Any]] = []



        indicator = alert.get(
            "indicator"
        )


        if indicator:

            artifacts.append(
                {
                    "type": "ioc",
                    "value": str(
                        indicator
                    ),
                }
            )



        source = alert.get(
            "source"
        )


        if source:

            artifacts.append(
                {
                    "type": "source",
                    "value": str(
                        source
                    ),
                }
            )



        severity = alert.get(
            "severity"
        )


        if severity:

            artifacts.append(
                {
                    "type": "severity",
                    "value": str(
                        severity
                    ),
                }
            )



        return artifacts