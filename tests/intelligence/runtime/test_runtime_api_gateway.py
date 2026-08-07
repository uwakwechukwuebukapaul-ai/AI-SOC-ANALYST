"""
Runtime API Gateway Tests
"""

from services.intelligence.runtime.runtime_api_gateway import (
    RuntimeAPIGateway,
)



def test_init():

    gateway = RuntimeAPIGateway()

    assert (
        gateway.requests
        ==
        0
    )



def test_register():

    gateway = RuntimeAPIGateway()


    gateway.register(
        "ping",
        lambda data: {
            "status":
                "ok"
        },
    )


    assert (
        "ping"
        in gateway.handlers
    )



def test_dispatch():

    gateway = RuntimeAPIGateway()


    gateway.register(
        "ping",
        lambda data: {
            "status":
                "ok"
        },
    )


    result = gateway.dispatch(
        "ping",
        {},
    )


    assert (
        result["status"]
        ==
        "ok"
    )



def test_missing_command():

    gateway = RuntimeAPIGateway()


    result = gateway.dispatch(
        "missing",
        {},
    )


    assert result is None



def test_health():

    gateway = RuntimeAPIGateway()


    result = gateway.health()


    assert "requests" in result

    assert "platform" in result



def test_clear():

    gateway = RuntimeAPIGateway()


    gateway.register(
        "test",
        lambda x: True,
    )


    gateway.clear()


    assert (
        len(
            gateway.handlers
        )
        ==
        0
    )



def test_status():

    gateway = RuntimeAPIGateway()


    result = gateway.status()


    assert "commands" in result

    assert "requests" in result