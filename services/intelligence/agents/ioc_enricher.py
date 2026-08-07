"""
IOC Enricher

Combines IOC classification and reputation into a single enrichment result.

Future integrations:
- VirusTotal
- AbuseIPDB
- AlienVault OTX
- MISP
- Internal Threat Intelligence
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict

from .ioc_classifier import IOCClassifier, IOCType
from .reputation_engine import ReputationEngine, Reputation


@dataclass(slots=True)
class IOCEnrichment:

    indicator: str

    indicator_type: IOCType

    reputation: Reputation

    confidence: float

    source: str

    attributes: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class IOCEnricher:
    """
    Offline IOC enrichment engine.
    """

    @classmethod
    def enrich(cls, indicator: str) -> IOCEnrichment:

        indicator = indicator.strip()

        indicator_type = IOCClassifier.classify(indicator)

        reputation = ReputationEngine.lookup(indicator)

        attributes = {
            "length": len(indicator),
            "normalized": indicator.lower(),
        }

        if indicator_type == IOCType.DOMAIN:
            attributes["top_level_domain"] = indicator.split(".")[-1]

        elif indicator_type == IOCType.EMAIL:
            attributes["domain"] = indicator.split("@")[-1]

        elif indicator_type == IOCType.URL:
            attributes["scheme"] = (
                "https"
                if indicator.lower().startswith("https://")
                else "http"
            )

        return IOCEnrichment(
            indicator=indicator,
            indicator_type=indicator_type,
            reputation=reputation.reputation,
            confidence=reputation.confidence,
            source=reputation.source,
            attributes=attributes,
        )