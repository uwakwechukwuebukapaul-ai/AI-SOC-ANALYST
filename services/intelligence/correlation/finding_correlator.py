"""
Sentinel DNA Finding Correlator

Correlates investigation findings
from multiple intelligence sources.
"""

from __future__ import annotations

from typing import Any


class FindingCorrelator:
    """
    Combines findings from agents.

    Future expansion:

    - ML similarity matching
    - ATT&CK mapping
    - graph correlation
    """


    def correlate(
        self,
        findings: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Remove duplicates and merge
        related findings.
        """

        correlated = []

        seen = set()


        for finding in findings:

            key = (
                finding.get("type"),
                finding.get("value"),
            )


            if key in seen:
                continue


            seen.add(key)


            correlated.append(
                finding
            )


        return correlated