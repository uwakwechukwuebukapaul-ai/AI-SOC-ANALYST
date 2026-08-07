from services.intelligence.runtime.runtime_gateway import (
    RuntimeGateway,
)


def test_gateway_init():

    gateway = RuntimeGateway()

    assert (
        gateway.controller
        is not None
    )



def test_start():

    gateway = RuntimeGateway()

    gateway.start()

    assert (
        gateway.controller.running
        is True
    )



def test_stop():

    gateway = RuntimeGateway()

    gateway.start()

    gateway.stop()

    assert (
        gateway.controller.running
        is False
    )



def test_health():

    gateway = RuntimeGateway()

    result = gateway.health()

    assert "running" in result

    assert "state" in result



def test_status():

    gateway = RuntimeGateway()

    result = gateway.status()

    assert "engine" in result

    assert "events" in result