"""
Sentinel DNA Finding Correlator

Correlates investigation findings
and removes duplicates safely.
"""

from __future__ import annotations

from typing import Any


class FindingCorrelator:
    """
    Finding correlation engine.

    Responsibilities:

    - normalize findings
    - remove duplicates
    - preserve investigation evidence
    """

    def correlate(
        self,
        findings: list[Any],
    ) -> list[Any]:
        """
        Correlate findings.

        Handles:
        - strings
        - dictionaries
        - objects
        """

        correlated = []

        seen = set()

        for finding in findings:

            key = self._build_key(
                finding
            )

            if key in seen:
                continue

            seen.add(key)

            correlated.append(
                finding
            )

        return correlated


    def _build_key(
        self,
        finding: Any,
    ):
        """
        Build hashable identity key.
        """

        if isinstance(
            finding,
            dict,
        ):
            return tuple(
                sorted(
                    (
                        key,
                        str(value),
                    )
                    for key, value in finding.items()
                )
            )


        if isinstance(
            finding,
            list,
        ):
            return tuple(
                self._build_key(item)
                for item in finding
            )


        if hasattr(
            finding,
            "__dict__",
        ):
            return tuple(
                sorted(
                    (
                        key,
                        str(value),
                    )
                    for key, value in finding.__dict__.items()
                )
            )


        return str(finding)