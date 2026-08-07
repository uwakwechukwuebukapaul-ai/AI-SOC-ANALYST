"""
Investigation finding aggregation.
"""

from __future__ import annotations

from typing import Any


class FindingAggregator:
    """
    Converts correlated intelligence into a normalized
    investigation finding.
    """

    def aggregate(
        self,
        investigation: dict[str, Any],
        intelligence: dict[str, Any],
        correlation: dict[str, Any],
        confidence: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(investigation, dict):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        findings: list[dict[str, Any]] = []

        for service_name, result in intelligence.items():
            if not isinstance(result, dict):
                continue

            finding = self._build_finding(
                service_name,
                result,
            )

            if finding:
                findings.append(finding)

        risk = self._resolve_risk(
            intelligence
        )

        return {
            "type": "unified_investigation_finding",
            "investigation": investigation,
            "risk": risk,
            "confidence": confidence,
            "findings": findings,
            "correlation": correlation,
            "finding_count": len(findings),
            "status": "completed",
        }

    def _build_finding(
        self,
        service_name: str,
        result: dict[str, Any],
    ) -> dict[str, Any] | None:
        signals: list[Any] = []

        if result.get("severity"):
            signals.append(
                result["severity"]
            )

        if result.get("matches"):
            signals.extend(
                result["matches"]
            )

        if result.get("techniques"):
            signals.extend(
                result["techniques"]
            )

        if result.get("score") is not None:
            signals.append(
                f"score:{result['score']}"
            )

        if result.get("risk_score") is not None:
            signals.append(
                f"risk_score:{result['risk_score']}"
            )

        if not signals:
            return None

        return {
            "source": service_name,
            "signals": signals,
            "status": result.get(
                "status",
                "completed",
            ),
        }

    @staticmethod
    def _resolve_risk(
        intelligence: dict[str, Any],
    ) -> str:
        severities = []

        for result in intelligence.values():
            if not isinstance(result, dict):
                continue

            severity = result.get("severity")

            if severity:
                severities.append(
                    str(severity).lower()
                )

        if "critical" in severities:
            return "critical"

        if "high" in severities:
            return "high"

        if "medium" in severities:
            return "medium"

        if severities:
            return "low"

        return "unknown"