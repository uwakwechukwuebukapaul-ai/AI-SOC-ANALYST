from services.governance.autonomous_security_governance_engine import (
    AutonomousSecurityGovernanceEngine
)


def test_create_policy():

    engine = AutonomousSecurityGovernanceEngine()

    policy = engine.create_policy(
        "Critical Containment Policy",
        "Require approval before isolation",
        "high"
    )

    assert (
        policy["name"]
        ==
        "Critical Containment Policy"
    )


def test_validate_action_policy():

    engine = AutonomousSecurityGovernanceEngine()

    result = engine.validate_action_policy(
        "automatic_containment",
        95
    )

    assert (
        result["decision"]
        ==
        "requires_approval"
    )


def test_risk_acceptance():

    engine = AutonomousSecurityGovernanceEngine()

    result = engine.create_risk_acceptance(
        "legacy vulnerability",
        "security_manager",
        "temporary exception"
    )

    assert (
        result["status"]
        ==
        "pending_review"
    )


def test_compliance_mapping():

    engine = AutonomousSecurityGovernanceEngine()

    result = engine.map_compliance_control(
        "MITRE ATT&CK",
        "T1059"
    )

    assert result["mapped"] is True


def test_override_control():

    engine = AutonomousSecurityGovernanceEngine()

    result = engine.override_control(
        "analyst01",
        "block_ip",
        "business exception"
    )

    assert (
        result["status"]
        ==
        "override_applied"
    )


def test_governance_history():

    engine = AutonomousSecurityGovernanceEngine()

    engine.create_policy(
        "Test Policy",
        "monitor"
    )

    history = engine.get_history()

    assert len(history) == 1