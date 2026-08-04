from services.governance.autonomous_security_governance_engine import (
    AutonomousSecurityGovernanceEngine,
)


def test_register_policy():
    engine = AutonomousSecurityGovernanceEngine()

    result = engine.register_policy(
        "POL-001",
        "Access Control Policy",
        "Identity",
        ["MFA Required"],
    )

    assert result["policy_id"] == "POL-001"


def test_map_compliance_control():
    engine = AutonomousSecurityGovernanceEngine()

    result = engine.map_compliance_control(
        "NIST",
        "AC-2",
        "Account Management",
    )

    assert result["framework"] == "NIST"


def test_analyze_governance_state():
    engine = AutonomousSecurityGovernanceEngine()

    result = engine.analyze_governance_state(
        {
            "critical_findings": 1,
            "missing_controls": 2,
        }
    )

    assert "governance_score" in result


def test_generate_ai_explanation():
    engine = AutonomousSecurityGovernanceEngine()

    result = engine.generate_ai_explanation(
        "Block malicious IP",
        "IOC matched threat intelligence",
        0.95,
    )

    assert result["confidence"] == 0.95


def test_record_risk_acceptance():
    engine = AutonomousSecurityGovernanceEngine()

    result = engine.record_risk_acceptance(
        "RISK-001",
        "Security Officer",
        "Business exception approved",
    )

    assert result["risk_id"] == "RISK-001"


def test_governance_history():
    engine = AutonomousSecurityGovernanceEngine()

    engine.register_policy(
        "POL-002",
        "Logging Policy",
        "Monitoring",
        ["Central Logging"],
    )

    history = engine.get_history()

    assert len(history) == 1