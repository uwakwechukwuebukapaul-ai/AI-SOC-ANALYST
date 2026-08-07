"""
Runtime Security Manager Tests
"""

from services.intelligence.runtime.runtime_security_manager import (
    RuntimeSecurityManager,
)



def test_init():

    manager = RuntimeSecurityManager()

    assert (
        manager.permissions
        ==
        {}
    )



def test_grant():

    manager = RuntimeSecurityManager()


    manager.grant(
        "agent",
        "execute",
    )


    assert (
        manager.allowed(
            "agent",
            "execute",
        )
        is True
    )



def test_revoke():

    manager = RuntimeSecurityManager()


    manager.grant(
        "agent",
        "execute",
    )


    manager.revoke(
        "agent",
        "execute",
    )


    assert (
        manager.allowed(
            "agent",
            "execute",
        )
        is False
    )



def test_policy():

    manager = RuntimeSecurityManager()


    manager.set_policy(
        "require_auth",
        True,
    )


    assert (
        manager.policy_enabled(
            "require_auth"
        )
        is True
    )



def test_clear():

    manager = RuntimeSecurityManager()


    manager.grant(
        "agent",
        "run",
    )


    manager.clear()


    assert (
        manager.permissions
        ==
        {}
    )



def test_status():

    manager = RuntimeSecurityManager()


    result = manager.status()


    assert "permissions" in result

    assert "policies" in result