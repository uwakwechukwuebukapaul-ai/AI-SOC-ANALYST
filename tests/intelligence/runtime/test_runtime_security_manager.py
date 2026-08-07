"""
Runtime Security Manager Tests
"""

from services.intelligence.runtime.runtime_security_manager import (
    RuntimeSecurityManager,
)



def test_init():

    manager = RuntimeSecurityManager()

    assert (
        manager.count()
        ==
        0
    )



def test_grant():

    manager = RuntimeSecurityManager()


    manager.grant(
        "analyst",
        "investigate",
    )


    assert (
        manager.allowed(
            "analyst",
            "investigate",
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



def test_missing_permission():

    manager = RuntimeSecurityManager()


    assert (
        manager.allowed(
            "unknown",
            "execute",
        )
        is False
    )



def test_identity_exists():

    manager = RuntimeSecurityManager()


    manager.grant(
        "service",
        "read",
    )


    assert (
        manager.identity_exists(
            "service"
        )
        is True
    )



def test_clear():

    manager = RuntimeSecurityManager()


    manager.grant(
        "test",
        "access",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeSecurityManager()


    result = manager.status()


    assert "identities" in result

    assert "count" in result