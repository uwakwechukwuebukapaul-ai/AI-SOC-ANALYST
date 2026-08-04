from services.response.response_governance_engine import (
    ResponseGovernanceEngine
)


def test_register_policy():

    engine = ResponseGovernanceEngine()

    result = engine.register_policy(
        "block_ioc",
        {
            "allowed_roles": [
                "analyst"
            ],
            "requires_approval": False
        }
    )

    assert result["registered"] is True


def test_permission_check():

    engine = ResponseGovernanceEngine()

    engine.register_policy(
        "isolate_endpoint",
        {
            "allowed_roles": [
                "admin"
            ]
        }
    )

    assert engine.check_permission(
        "isolate_endpoint",
        "admin"
    ) is True


def test_blocked_permission():

    engine = ResponseGovernanceEngine()

    engine.register_policy(
        "isolate_endpoint",
        {
            "allowed_roles": [
                "admin"
            ]
        }
    )

    assert engine.check_permission(
        "isolate_endpoint",
        "analyst"
    ) is False


def test_authorized_action():

    engine = ResponseGovernanceEngine()

    engine.register_policy(
        "block_ioc",
        {
            "allowed_roles": [
                "analyst"
            ],
            "requires_approval": False
        }
    )

    result = engine.authorize_action(
        "block_ioc",
        "analyst"
    )

    assert result["authorized"] is True


def test_approval_required():

    engine = ResponseGovernanceEngine()

    engine.register_policy(
        "isolate_endpoint",
        {
            "allowed_roles": [
                "admin"
            ],
            "requires_approval": True
        }
    )

    result = engine.authorize_action(
        "isolate_endpoint",
        "admin"
    )

    assert result["authorized"] is False


def test_audit_history():

    engine = ResponseGovernanceEngine()

    engine.register_policy(
        "notify_analyst",
        {
            "allowed_roles": [
                "analyst"
            ],
            "requires_approval": False
        }
    )

    engine.authorize_action(
        "notify_analyst",
        "analyst"
    )

    assert len(
        engine.get_audit_history()
    ) == 1