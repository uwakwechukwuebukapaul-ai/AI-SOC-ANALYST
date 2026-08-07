"""
Runtime Identity Manager Tests
"""

from services.intelligence.runtime.runtime_identity_manager import (
    RuntimeIdentityManager,
)



def test_init():

    manager = RuntimeIdentityManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimeIdentityManager()


    manager.register(
        "ai_investigator",
        "agent",
    )


    assert (
        manager.exists(
            "ai_investigator"
        )
        is True
    )



def test_role():

    manager = RuntimeIdentityManager()


    manager.register(
        "analyst01",
        "analyst",
    )


    assert (
        manager.role(
            "analyst01"
        )
        ==
        "analyst"
    )



def test_metadata():

    manager = RuntimeIdentityManager()


    manager.register(
        "connector_service",
        "service",
        {
            "version":
                "1.0"
        },
    )


    assert (
        manager.metadata(
            "connector_service"
        )["version"]
        ==
        "1.0"
    )



def test_remove():

    manager = RuntimeIdentityManager()


    manager.register(
        "test",
        "agent",
    )


    manager.remove(
        "test"
    )


    assert (
        manager.exists(
            "test"
        )
        is False
    )



def test_clear():

    manager = RuntimeIdentityManager()


    manager.register(
        "test",
        "agent",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeIdentityManager()


    result = manager.status()


    assert "identities" in result

    assert "count" in result