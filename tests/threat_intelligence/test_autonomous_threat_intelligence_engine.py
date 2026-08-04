from services.threat_intelligence.autonomous_threat_intelligence_engine import (
    AutonomousThreatIntelligenceEngine
)



def test_register_indicator():

    engine = AutonomousThreatIntelligenceEngine()

    result = engine.register_indicator(
        "ip",
        "192.168.1.10",
        0.9
    )

    assert result["status"] == "active"



def test_analyze_indicator():

    engine = AutonomousThreatIntelligenceEngine()

    indicator = {
        "value": "malicious.com",
        "confidence": 0.9
    }

    result = engine.analyze_indicator(
        indicator
    )

    assert result["risk"] == "high"



def test_create_threat_actor_profile():

    engine = AutonomousThreatIntelligenceEngine()

    result = engine.create_threat_actor_profile(
        "APT_TEST",
        [
            "phishing"
        ]
    )

    assert result["actor"] == "APT_TEST"



def test_map_attack_techniques():

    engine = AutonomousThreatIntelligenceEngine()

    result = engine.map_attack_techniques(
        [
            "phishing"
        ]
    )

    assert result[0]["attack_id"] == "T1566"



def test_track_campaign():

    engine = AutonomousThreatIntelligenceEngine()

    result = engine.track_campaign(
        "Operation_Test",
        [
            "ioc1"
        ]
    )

    assert result["status"] == "monitoring"



def test_threat_intelligence_history():

    engine = AutonomousThreatIntelligenceEngine()

    engine.register_indicator(
        "hash",
        "abc123",
        0.8
    )

    history = engine.get_history()

    assert len(history) > 0