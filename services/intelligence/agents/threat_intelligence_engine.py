"""
Threat Intelligence Engine

Converts IOC enrichment into enterprise threat assessments.

Future integrations:

- VirusTotal
- MISP
- OTX
- AbuseIPDB
- URLHaus
- Internal Threat Intelligence
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .ioc_enricher import IOCEnrichment
from .reputation_engine import Reputation
from .threat_level import ThreatLevel


@dataclass(slots=True)
class ThreatAssessment:
    """
    Threat assessment produced from IOC enrichment.
    """

    indicator: str

    threat_level: ThreatLevel

    confidence: float

    reputation: Reputation

    reason: str

    score: int

    def to_dict(self) -> dict:
        return {
            "indicator": self.indicator,
            "threat_level": self.threat_level.value,
            "confidence": self.confidence,
            "reputation": self.reputation.value,
            "reason": self.reason,
            "score": self.score,
        }


class ThreatIntelligenceEngine:
    """
    Enterprise threat intelligence engine.
    """

    @classmethod
    def assess(
        cls,
        enrichment: IOCEnrichment,
    ) -> ThreatAssessment:

        reputation = enrichment.reputation

        if reputation == Reputation.MALICIOUS:
            level = ThreatLevel.CRITICAL
            reason = "Known malicious IOC."

        elif reputation == Reputation.SUSPICIOUS:
            level = ThreatLevel.HIGH
            reason = "Suspicious IOC."

        elif reputation == Reputation.BENIGN:
            level = ThreatLevel.LOW
            reason = "Known benign IOC."

        else:
            level = ThreatLevel.MEDIUM
            reason = "Unknown reputation."

        return ThreatAssessment(
            indicator=enrichment.indicator,
            threat_level=level,
            confidence=enrichment.confidence,
            reputation=reputation,
            reason=reason,
            score=level.score,
        )

    @classmethod
    def assess_many(
        cls,
        enrichments: List[IOCEnrichment],
    ) -> List[ThreatAssessment]:

        return [
            cls.assess(item)
            for item in enrichments
        ]

    @classmethod
    def overall_level(
        cls,
        assessments: List[ThreatAssessment],
    ) -> ThreatLevel:

        if not assessments:
            return ThreatLevel.INFORMATIONAL

        return ThreatLevel.highest(
            [
                assessment.threat_level
                for assessment in assessments
            ]
        )

    @classmethod
    def average_confidence(
        cls,
        assessments: List[ThreatAssessment],
    ) -> float:

        if not assessments:
            return 0.0

        return round(
            sum(a.confidence for a in assessments)
            / len(assessments),
            2,
        )

    @classmethod
    def total_score(
        cls,
        assessments: List[ThreatAssessment],
    ) -> int:

        return sum(
            assessment.score
            for assessment in assessments
        )