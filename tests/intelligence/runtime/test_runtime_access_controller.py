"""
Runtime Access Controller Tests
"""

from services.intelligence.runtime.runtime_access_controller import (
    RuntimeAccessController,
)



def test_init():

    controller = RuntimeAccessController()

    assert (
        controller.checks
        ==
        0
    )



def test_grant_access():

    controller = RuntimeAccessController()


    controller.grant(
        "agent",
        "execute",
    )


    assert (
        controller.security.allowed(
            "agent",
            "execute",
        )
        is True
    )



def test_authorize_success():

    controller = RuntimeAccessController()


    controller.grant(
        "agent",
        "execute",
    )


    result = controller.authorize(
        "agent",
        "execute",
    )


    assert (
        result
        is True
    )



def test_authorize_denied():

    controller = RuntimeAccessController()


    result = controller.authorize(
        "agent",
        "execute",
    )


    assert (
        result
        is False
    )



def test_policy_check():

    controller = RuntimeAccessController()


    controller.grant(
        "agent",
        "execute",
    )


    controller.register_policy(
        "safe",
        lambda ctx: True,
    )


    result = controller.authorize(
        "agent",
        "execute",
        "safe",
    )


    assert (
        result
        is True
    )



def test_clear():

    controller = RuntimeAccessController()


    controller.grant(
        "agent",
        "execute",
    )


    controller.clear()


    assert (
        controller.checks
        ==
        0
    )



def test_status():

    controller = RuntimeAccessController()


    result = controller.status()


    assert "checks" in result

    assert "security" in result

    assert "policies" in result