"""
Runtime Security Orchestrator Tests
"""

from services.intelligence.runtime.runtime_security_orchestrator import (
    RuntimeSecurityOrchestrator,
)



def test_init():

    security = RuntimeSecurityOrchestrator()

    assert (
        len(
            security.policies
        )
        ==
        0
    )



def test_policy():

    security = RuntimeSecurityOrchestrator()


    security.add_policy(
        "require_approval",
        True,
    )


    assert (
        security.policy_enabled(
            "require_approval"
        )
        is True
    )



def test_grant_permission():

    security = RuntimeSecurityOrchestrator()


    security.grant(
        "ai_agent",
        "block_ip",
    )


    assert (
        security.authorize(
            "ai_agent",
            "block_ip",
        )
        is True
    )



def test_denied_permission():

    security = RuntimeSecurityOrchestrator()


    assert (
        security.authorize(
            "agent",
            "delete_case",
        )
        is False
    )



def test_clear():

    security = RuntimeSecurityOrchestrator()


    security.grant(
        "agent",
        "test",
    )


    security.clear()


    assert (
        security.authorize(
            "agent",
            "test",
        )
        is False
    )



def test_status():

    security = RuntimeSecurityOrchestrator()


    result = security.status()


    assert "policies" in result

    assert "actors" in result