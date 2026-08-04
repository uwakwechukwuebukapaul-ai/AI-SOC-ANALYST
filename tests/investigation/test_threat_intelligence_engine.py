from services.investigation.threat_intelligence_engine import ThreatIntelligenceEngine


def test_analyze_ioc():

    engine = ThreatIntelligenceEngine()

    result = engine.analyze_ioc(
        "malicious-example.com"
    )

    assert result["ioc"] == "malicious-example.com"


def test_detect_ioc_type():

    engine = ThreatIntelligenceEngine()

    result = engine.detect_ioc_type(
        "192.168.1.10"
    )

    assert result == "IP"


def test_reputation_check():

    engine = ThreatIntelligenceEngine()

    result = engine.check_reputation(
        "malware-domain.xyz"
    )

    assert "reputation" in result


def test_threat_classification():

    engine = ThreatIntelligenceEngine()

    result = engine.classify_threat(
        "credential phishing"
    )

    assert result["category"] == "Phishing"


def test_confidence_score():

    engine = ThreatIntelligenceEngine()

    score = engine.calculate_confidence(
        "HIGH"
    )

    assert score >= 80


def test_intelligence_history():

    engine = ThreatIntelligenceEngine()

    engine.analyze_ioc(
        "test-domain.com"
    )

    history = engine.get_history()

    assert len(history) == 1