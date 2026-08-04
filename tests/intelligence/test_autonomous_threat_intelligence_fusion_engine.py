from services.intelligence.autonomous_threat_intelligence_fusion_engine import (
    AutonomousThreatIntelligenceFusionEngine
)


def test_enrich_ioc():

    engine = AutonomousThreatIntelligenceFusionEngine()

    result = engine.enrich_ioc(
        "malicious-domain.xyz",
        "domain"
    )

    assert result["reputation"] == "malicious"


def test_ip_reputation_analysis():

    engine = AutonomousThreatIntelligenceFusionEngine()

    result = engine.analyze_ip_reputation(
        "185.10.10.10"
    )

    assert result["status"] == "analyzed"


def test_hash_analysis():

    engine = AutonomousThreatIntelligenceFusionEngine()

    result = engine.analyze_hash(
        "a" * 32
    )

    assert result["malware_detected"] is True


def test_threat_actor_mapping():

    engine = AutonomousThreatIntelligenceFusionEngine()

    result = engine.map_threat_actor(
        "phishing campaign"
    )

    assert result["threat_actor"] == "APT28"


def test_confidence_scoring():

    engine = AutonomousThreatIntelligenceFusionEngine()

    intelligence = engine.enrich_ioc(
        "evil-domain.top"
    )

    result = engine.calculate_confidence(
        intelligence
    )

    assert result["confidence_score"] == 100


def test_intelligence_history():

    engine = AutonomousThreatIntelligenceFusionEngine()

    engine.enrich_ioc(
        "test-domain.com"
    )

    assert len(engine.get_history()) == 1