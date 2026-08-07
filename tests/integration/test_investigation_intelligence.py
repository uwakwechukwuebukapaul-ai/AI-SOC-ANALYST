"""
Integration tests for Investigation Intelligence.
"""

from services.investigation_intelligence import (
    ConfidenceResolver,
    EvidenceCorrelator,
    FindingAggregator,
    IntelligenceCoordinator,
    InvestigationEngine,
)


def test_confidence_resolver():
    resolver = ConfidenceResolver()

    result = resolver.resolve(
        {
            "risk": {
                "confidence": 0.90,
            },
            "mitre": {
                "confidence": 0.80,
            },
        }
    )

    assert result["score"] == 0.85
    assert result["level"] == "high"
    assert result["sources"] == 2


def test_evidence_correlation():
    correlator = EvidenceCorrelator()

    result = correlator.correlate(
        {
            "indicator": "powershell",
        },
        {
            "mitre": {
                "techniques": ["T1059"],
            },
            "detection": {
                "matches": [
                    "suspicious_powershell"
                ],
            },
        },
    )

    assert result["signal_count"] == 2
    assert result["relationship_count"] == 1


def test_finding_aggregation():
    aggregator = FindingAggregator()

    result = aggregator.aggregate(
        {
            "indicator": "powershell",
        },
        {
            "risk": {
                "severity": "high",
                "risk_score": 90,
                "status": "completed",
            },
            "mitre": {
                "techniques": ["T1059"],
            },
        },
        {
            "signal_count": 2,
            "relationship_count": 0,
        },
        {
            "score": 0.85,
            "level": "high",
            "sources": 2,
        },
    )

    assert result["type"] == (
        "unified_investigation_finding"
    )

    assert result["risk"] == "high"
    assert result["finding_count"] == 2


def test_intelligence_coordinator():
    coordinator = IntelligenceCoordinator()

    coordinator.register(
        "risk",
        lambda investigation: {
            "risk_score": 90,
            "severity": "critical",
            "confidence": 0.95,
            "status": "completed",
        },
    )

    coordinator.register(
        "mitre",
        lambda investigation: {
            "techniques": ["T1059"],
            "confidence": 0.85,
        },
    )

    result = coordinator.analyze(
        {
            "source": "endpoint",
            "indicator": "powershell",
        }
    )

    assert result["status"] == "completed"
    assert set(
        result["intelligence"].keys()
    ) == {
        "risk",
        "mitre",
    }

    assert result["confidence"]["level"] == "high"
    assert result["finding"]["risk"] == "critical"


def test_investigation_engine():
    engine = InvestigationEngine()

    engine.register_provider(
        "risk",
        lambda investigation: {
            "risk_score": 90,
            "severity": "critical",
            "confidence": 0.95,
        },
    )

    engine.register_provider(
        "detection",
        lambda investigation: {
            "matches": [
                "IOC indicator detected",
            ],
            "confidence": 0.80,
        },
    )

    result = engine.investigate(
        {
            "source": "endpoint",
            "indicator": "powershell",
        }
    )

    assert (
        result["type"]
        == "investigation_intelligence"
    )

    assert result["status"] == "completed"
    assert result["finding"]["risk"] == "critical"
    assert result["finding"]["finding_count"] == 2
    assert result["confidence"]["level"] == "high"


def test_provider_validation():
    coordinator = IntelligenceCoordinator()

    try:
        coordinator.register(
            "",
            lambda investigation: {},
        )
        assert False
    except ValueError:
        pass

    try:
        coordinator.register(
            "invalid",
            "not-callable",
        )
        assert False
    except TypeError:
        pass