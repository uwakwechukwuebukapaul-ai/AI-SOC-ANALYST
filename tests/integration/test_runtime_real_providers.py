"""
Integration tests for Sentinel DNA's real runtime providers.
"""

from __future__ import annotations

from services.investigation_runtime.providers import (
    create_default_service_bridge,
)


def test_default_service_bridge_registers_core_services():
    bridge = create_default_service_bridge()

    services = bridge.available_services()

    assert "risk_intelligence" in services
    assert "mitre_intelligence" in services
    assert "detection_engineering" in services
    assert "threat_hunting" in services


def test_default_provider_capabilities():
    bridge = create_default_service_bridge()

    capabilities = bridge.available_capabilities()

    assert capabilities["risk_intelligence"] == (
        "risk_assessment"
    )

    assert capabilities["mitre_intelligence"] == (
        "attack_mapping"
    )

    assert capabilities["detection_engineering"] == (
        "detection_analysis"
    )

    assert capabilities["threat_hunting"] == (
        "threat_hunting"
    )


def test_risk_provider_executes():
    bridge = create_default_service_bridge()

    result = bridge.execute(
        "risk_intelligence",
        {
            "risk_score": 80,
            "severity": "high",
        },
    )

    assert result["type"] == "risk_assessment"
    assert result["score"] == 100
    assert result["severity"] == "critical"


def test_detection_provider_executes():
    bridge = create_default_service_bridge()

    result = bridge.execute(
        "detection_engineering",
        {
            "indicator": "malicious.example",
            "severity": "high",
        },
    )

    assert result["type"] == "detection_analysis"
    assert "IOC indicator detected" in result["matches"]


def test_mitre_provider_executes():
    bridge = create_default_service_bridge()

    result = bridge.execute(
        "mitre_intelligence",
        {
            "technique_signal": "powershell",
        },
    )

    assert "techniques" in result
    assert "tactics" in result
    assert "attack_path" in result
    assert "coverage" in result


def test_threat_hunting_provider_executes():
    bridge = create_default_service_bridge()

    result = bridge.execute(
        "threat_hunting",
        {
            "hunt_hypothesis": {
                "indicator": "malicious.example",
            },
            "hunt_data": [
                {
                    "host": "endpoint-01",
                    "indicator": "malicious.example",
                },
                {
                    "host": "endpoint-02",
                    "indicator": "benign.example",
                },
            ],
        },
    )

    assert result["type"] == "threat_hunt"
    assert len(result["matches"]) == 1


def test_all_core_providers_execute():
    bridge = create_default_service_bridge()

    investigation = {
        "risk_score": 70,
        "severity": "high",
        "technique_signal": "powershell",
        "indicator": "malicious.example",
        "hunt_hypothesis": {
            "indicator": "malicious.example",
        },
        "hunt_data": [
            {
                "indicator": "malicious.example",
            },
        ],
    }

    risk = bridge.execute(
        "risk_intelligence",
        investigation,
    )

    mitre = bridge.execute(
        "mitre_intelligence",
        investigation,
    )

    detection = bridge.execute(
        "detection_engineering",
        investigation,
    )

    hunting = bridge.execute(
        "threat_hunting",
        investigation,
    )

    assert risk["status"] == "completed"
    assert "techniques" in mitre
    assert detection["status"] == "completed"
    assert hunting["status"] == "completed"