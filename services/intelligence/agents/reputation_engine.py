"""
Offline Reputation Engine

Provides deterministic reputation scoring for Indicators of Compromise (IOCs).

This implementation is intentionally offline so unit tests remain fast,
repeatable, and independent of third-party services.

Future integrations can replace or augment this engine with:
- VirusTotal
- AbuseIPDB
- AlienVault OTX
- MISP
- URLhaus
- Spamhaus
- Internal Threat Intelligence
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .ioc_classifier import IOCClassifier, IOCType


class Reputation(str, Enum):
    MALICIOUS = "malicious"
    SUSPICIOUS = "suspicious"
    UNKNOWN = "unknown"
    BENIGN = "benign"


@dataclass(slots=True)
class ReputationResult:
    indicator: str
    indicator_type: IOCType
    reputation: Reputation
    confidence: float
    source: str = "offline"


class ReputationEngine:
    """
    Offline IOC reputation engine.
    """

    MALICIOUS_DOMAINS = {
        "evil.com",
        "malware.test",
        "phishing.test",
        "bad-domain.xyz",
    }

    MALICIOUS_IPS = {
        "185.220.101.1",
        "45.155.205.233",
        "103.21.244.1",
    }

    MALICIOUS_HASHES = {
        "44d88612fea8a8f36de82e1278abb02f",
    }

    SUSPICIOUS_TLDS = {
        ".xyz",
        ".top",
        ".click",
        ".zip",
        ".ru",
    }

    @classmethod
    def lookup(cls, indicator: str) -> ReputationResult:
        """
        Returns a reputation assessment for the supplied IOC.
        """

        indicator = indicator.strip()

        ioc_type = IOCClassifier.classify(indicator)

        if ioc_type == IOCType.IP:
            return cls._lookup_ip(indicator)

        if ioc_type == IOCType.DOMAIN:
            return cls._lookup_domain(indicator)

        if ioc_type == IOCType.URL:
            return cls._lookup_url(indicator)

        if ioc_type == IOCType.EMAIL:
            return cls._lookup_email(indicator)

        if ioc_type in (
            IOCType.MD5,
            IOCType.SHA1,
            IOCType.SHA256,
        ):
            return cls._lookup_hash(indicator, ioc_type)

        return ReputationResult(
            indicator=indicator,
            indicator_type=ioc_type,
            reputation=Reputation.UNKNOWN,
            confidence=25.0,
        )

    @classmethod
    def _lookup_ip(cls, ip: str) -> ReputationResult:

        if ip in cls.MALICIOUS_IPS:
            return ReputationResult(
                indicator=ip,
                indicator_type=IOCType.IP,
                reputation=Reputation.MALICIOUS,
                confidence=99.0,
            )

        return ReputationResult(
            indicator=ip,
            indicator_type=IOCType.IP,
            reputation=Reputation.UNKNOWN,
            confidence=55.0,
        )

    @classmethod
    def _lookup_domain(cls, domain: str) -> ReputationResult:

        lower = domain.lower()

        if lower in cls.MALICIOUS_DOMAINS:
            return ReputationResult(
                indicator=domain,
                indicator_type=IOCType.DOMAIN,
                reputation=Reputation.MALICIOUS,
                confidence=98.0,
            )

        if any(lower.endswith(tld) for tld in cls.SUSPICIOUS_TLDS):
            return ReputationResult(
                indicator=domain,
                indicator_type=IOCType.DOMAIN,
                reputation=Reputation.SUSPICIOUS,
                confidence=82.0,
            )

        return ReputationResult(
            indicator=domain,
            indicator_type=IOCType.DOMAIN,
            reputation=Reputation.BENIGN,
            confidence=70.0,
        )

    @classmethod
    def _lookup_url(cls, url: str) -> ReputationResult:

        lower = url.lower()

        if any(tld in lower for tld in cls.SUSPICIOUS_TLDS):
            return ReputationResult(
                indicator=url,
                indicator_type=IOCType.URL,
                reputation=Reputation.SUSPICIOUS,
                confidence=84.0,
            )

        return ReputationResult(
            indicator=url,
            indicator_type=IOCType.URL,
            reputation=Reputation.UNKNOWN,
            confidence=60.0,
        )

    @classmethod
    def _lookup_email(cls, email: str) -> ReputationResult:

        domain = email.split("@")[-1].lower()

        if domain in cls.MALICIOUS_DOMAINS:
            return ReputationResult(
                indicator=email,
                indicator_type=IOCType.EMAIL,
                reputation=Reputation.MALICIOUS,
                confidence=97.0,
            )

        return ReputationResult(
            indicator=email,
            indicator_type=IOCType.EMAIL,
            reputation=Reputation.UNKNOWN,
            confidence=65.0,
        )

    @classmethod
    def _lookup_hash(
        cls,
        value: str,
        hash_type: IOCType,
    ) -> ReputationResult:

        if value.lower() in cls.MALICIOUS_HASHES:
            return ReputationResult(
                indicator=value,
                indicator_type=hash_type,
                reputation=Reputation.MALICIOUS,
                confidence=100.0,
            )

        return ReputationResult(
            indicator=value,
            indicator_type=hash_type,
            reputation=Reputation.UNKNOWN,
            confidence=60.0,
        )