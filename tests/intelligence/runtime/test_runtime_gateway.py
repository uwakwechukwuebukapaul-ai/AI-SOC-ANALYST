"""
Runtime Gateway Tests
"""

from services.intelligence.runtime.runtime_gateway import (
    RuntimeGateway,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "source": "test"
        }
    )



def test_gateway_init():

    gateway = RuntimeGateway()

    assert gateway.controller is not None



def test_start():

    gateway = RuntimeGateway()

    gateway.start()

    assert (
        gateway.controller.initialized
        is True
    )



def test_stop():

    gateway = RuntimeGateway()

    gateway.start()

    gateway.stop()

    assert (
        gateway.controller.initialized
        is False
    )



def test_submit():

    gateway = RuntimeGateway()

    result = gateway.submit(
        create_task()
    )

    assert (
        result["submitted"]
        is True
    )



def test_execute():

    gateway = RuntimeGateway()


    gateway.register_handler(
        "analysis",
        lambda task: "completed"
    )


    result = gateway.execute(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_status():

    gateway = RuntimeGateway()

    result = gateway.status()

    assert (
        "initialized"
        in result
    )