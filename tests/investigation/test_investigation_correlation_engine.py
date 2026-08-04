from services.investigation.investigation_correlation_engine import (
    InvestigationCorrelationEngine
)


def test_create_correlation():

    engine = InvestigationCorrelationEngine()

    result = engine.create_correlation(
        "INC-001",
        ["email", "ioc"]
    )

    assert result["investigation_id"] == "INC-001"
    assert result["status"] == "created"


def test_add_evidence_relationship():

    engine = InvestigationCorrelationEngine()

    engine.create_correlation(
        "INC-002",
        ["malware"]
    )

    relationship = engine.add_relationship(
        "INC-002",
        "malware",
        "domain",
        "communicates_with"
    )

    assert relationship["type"] == "communicates_with"


def test_correlate_iocs():

    engine = InvestigationCorrelationEngine()

    engine.create_correlation(
        "INC-003",
        ["ioc"]
    )

    result = engine.correlate_iocs(
        "INC-003",
        [
            "evil.com",
            "192.168.1.10"
        ]
    )

    assert len(result) == 2


def test_detect_attack_pattern():

    engine = InvestigationCorrelationEngine()

    engine.create_correlation(
        "INC-004",
        ["attack"]
    )

    result = engine.detect_attack_pattern(
        "INC-004",
        [
            "T1566",
            "T1059"
        ]
    )

    assert result["confidence"] == 40


def test_generate_correlation_score():

    engine = InvestigationCorrelationEngine()

    engine.create_correlation(
        "INC-005",
        ["ioc"]
    )

    engine.correlate_iocs(
        "INC-005",
        [
            "test.com"
        ]
    )

    score = engine.generate_correlation_score(
        "INC-005"
    )

    assert score > 0


def test_correlation_history():

    engine = InvestigationCorrelationEngine()

    engine.create_correlation(
        "INC-006",
        ["evidence"]
    )

    history = engine.get_history()

    assert len(history) == 1