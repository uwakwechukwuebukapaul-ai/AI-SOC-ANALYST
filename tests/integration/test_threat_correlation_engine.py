from services.threat_intelligence import (
    ThreatCorrelationEngine
)


def test_ioc_extraction():

    engine = ThreatCorrelationEngine()

    result = engine.extract_iocs(
        {
            "ip": "192.168.1.10",
            "domain": "evil.example"
        }
    )

    assert len(result) == 2



def test_threat_correlation():

    engine = ThreatCorrelationEngine()

    result = engine.correlate(
        {
            "ip": "192.168.1.10",
            "hash": "abc123"
        }
    )

    assert result["status"] == "completed"
    assert result["risk_score"] > 0