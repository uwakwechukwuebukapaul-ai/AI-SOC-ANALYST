"""
Runtime Security Manager Tests
"""

from services.intelligence.runtime.runtime_security_manager import (
    RuntimeSecurityManager,
)



def test_manager_init():

    manager = RuntimeSecurityManager()

    assert (
        manager.identities
        ==
        {}
    )



def test_register_identity():

    manager = RuntimeSecurityManager()


    manager.register_identity(
        "analyst",
        [
            "execute",
            "investigate",
        ],
    )


    assert (
        "analyst"
        in
        manager.identities
    )



def test_authorize_allowed():

    manager = RuntimeSecurityManager()


    manager.register_identity(
        "agent",
        [
            "scan",
        ],
    )


    result = manager.authorize(
        "agent",
        "scan",
    )


    assert result is True



def test_authorize_denied():

    manager = RuntimeSecurityManager()


    manager.register_identity(
        "agent",
        [
            "scan",
        ],
    )


    result = manager.authorize(
        "agent",
        "delete",
    )


    assert result is False



def test_revoke():

    manager = RuntimeSecurityManager()


    manager.register_identity(
        "user",
        [],
    )


    manager.revoke(
        "user"
    )


    assert (
        "user"
        not in
        manager.identities
    )



def test_status():

    manager = RuntimeSecurityManager()


    result = manager.status()


    assert "identities" in result

    assert "registered" in result