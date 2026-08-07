"""
Coordinates Sentinel DNA intelligence services.
"""

from __future__ import annotations

from typing import Any, Callable

from .confidence_resolver import ConfidenceResolver
from .evidence_correlator import EvidenceCorrelator
from .finding_aggregator import FindingAggregator


class IntelligenceCoordinator:
    """
    Coordinates independent intelligence providers.

    Providers can either be executed directly through
    ``analyze`` or pre-executed results can be supplied
    through ``analyze_results``.
    """

    def __init__(
        self,
        correlator: EvidenceCorrelator | None = None,
        aggregator: FindingAggregator | None = None,
        confidence_resolver: ConfidenceResolver | None = None,
    ) -> None:
        self.correlator = (
            correlator or EvidenceCorrelator()
        )

        self.aggregator = (
            aggregator or FindingAggregator()
        )

        self.confidence_resolver = (
            confidence_resolver
            or ConfidenceResolver()
        )

        self._providers: dict[
            str,
            Callable[
                [dict[str, Any]],
                dict[str, Any],
            ],
        ] = {}

    def register(
        self,
        name: str,
        provider: Callable[
            [dict[str, Any]],
            dict[str, Any],
        ],
    ) -> None:
        if not name:
            raise ValueError(
                "Provider name is required."
            )

        if not callable(provider):
            raise TypeError(
                "Provider must be callable."
            )

        self._providers[name] = provider

    def unregister(
        self,
        name: str,
    ) -> Callable | None:
        return self._providers.pop(
            name,
            None,
        )

    def providers(self) -> list[str]:
        return list(
            self._providers.keys()
        )

    def analyze(
        self,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(
            investigation,
            dict,
        ):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        intelligence: dict[
            str,
            dict[str, Any],
        ] = {}

        for name, provider in (
            self._providers.items()
        ):
            result = provider(
                investigation
            )

            if not isinstance(
                result,
                dict,
            ):
                raise TypeError(
                    f"Provider '{name}' must "
                    "return a dictionary."
                )

            intelligence[name] = result

        return self.analyze_results(
            investigation,
            intelligence,
        )

    def analyze_results(
        self,
        investigation: dict[str, Any],
        intelligence: dict[
            str,
            dict[str, Any],
        ],
    ) -> dict[str, Any]:
        """
        Analyze already-executed intelligence results.

        This is the critical boundary between runtime
        execution and intelligence reasoning.
        """

        if not isinstance(
            investigation,
            dict,
        ):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        if not isinstance(
            intelligence,
            dict,
        ):
            raise TypeError(
                "Intelligence must be a dictionary."
            )

        for name, result in (
            intelligence.items()
        ):
            if not isinstance(
                result,
                dict,
            ):
                raise TypeError(
                    f"Intelligence result "
                    f"'{name}' must be a dictionary."
                )

        correlation = (
            self.correlator.correlate(
                investigation,
                intelligence,
            )
        )

        confidence = (
            self.confidence_resolver.resolve(
                intelligence
            )
        )

        finding = self.aggregator.aggregate(
            investigation,
            intelligence,
            correlation,
            confidence,
        )

        return {
            "intelligence": intelligence,
            "correlation": correlation,
            "confidence": confidence,
            "finding": finding,
            "status": "completed",
        }