from services.investigation.autonomous_investigation_intelligence_engine import (
    AutonomousInvestigationIntelligenceEngine
)

from services.threat_intelligence import *


def test_threat_intelligence_correlation():

    engine = AutonomousInvestigationIntelligenceEngine()

    evidence = {
        "event": "malicious_login",
        "ip": "192.168.1.10",
        "severity": "high"
    }

    result = engine.analyze(evidence)

    assert result["status"] == "completed"
    assert result["severity"] == "high"


def test_ioc_extraction_flow():

    engine = AutonomousInvestigationIntelligenceEngine()

    alert = {
        "indicator": "192.168.1.10",
        "type": "ip"
    }

    result = engine.investigate(alert)

    assert result["status"] == "completed"
    assert result["type"] == "investigation"