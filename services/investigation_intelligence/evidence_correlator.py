"""
Evidence correlation for Sentinel DNA investigations.
"""

from __future__ import annotations

from typing import Any


class EvidenceCorrelator:
    """
    Correlates outputs produced by independent intelligence
    services.

    Correlation is based on observable signals rather than
    coupling to a specific service implementation.
    """

    def correlate(
        self,
        investigation: dict[str, Any],
        intelligence: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(investigation, dict):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        if not isinstance(intelligence, dict):
            raise TypeError(
                "Intelligence must be a dictionary."
            )

        signals: list[dict[str, Any]] = []
        relationships: list[dict[str, Any]] = []

        for service_name, result in intelligence.items():
            if not isinstance(result, dict):
                continue

            signals.extend(
                self._extract_signals(
                    service_name,
                    result,
                )
            )

        for index, left in enumerate(signals):
            for right in signals[index + 1:]:
                relationship = self._relate(
                    left,
                    right,
                )

                if relationship:
                    relationships.append(
                        relationship
                    )

        return {
            "investigation": investigation,
            "signals": signals,
            "relationships": relationships,
            "signal_count": len(signals),
            "relationship_count": len(
                relationships
            ),
        }

    def _extract_signals(
        self,
        service_name: str,
        result: dict[str, Any],
    ) -> list[dict[str, Any]]:
        signals: list[dict[str, Any]] = []

        if result.get("severity"):
            signals.append(
                {
                    "source": service_name,
                    "type": "severity",
                    "value": result["severity"],
                }
            )

        if result.get("score") is not None:
            signals.append(
                {
                    "source": service_name,
                    "type": "score",
                    "value": result["score"],
                }
            )

        if result.get("risk_score") is not None:
            signals.append(
                {
                    "source": service_name,
                    "type": "risk_score",
                    "value": result["risk_score"],
                }
            )

        for technique in result.get(
            "techniques",
            [],
        ):
            signals.append(
                {
                    "source": service_name,
                    "type": "mitre_technique",
                    "value": technique,
                }
            )

        for match in result.get(
            "matches",
            [],
        ):
            signals.append(
                {
                    "source": service_name,
                    "type": "detection_match",
                    "value": match,
                }
            )

        return signals

    @staticmethod
    def _relate(
        left: dict[str, Any],
        right: dict[str, Any],
    ) -> dict[str, Any] | None:
        if left["value"] == right["value"]:
            return {
                "type": "shared_signal",
                "left": left,
                "right": right,
            }

        if {
            left["type"],
            right["type"],
        } == {
            "mitre_technique",
            "detection_match",
        }:
            return {
                "type": "detection_mitre_correlation",
                "left": left,
                "right": right,
            }

        return None