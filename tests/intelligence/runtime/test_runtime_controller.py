"""
Runtime Controller Tests
"""

from services.intelligence.runtime.runtime_controller import (
    RuntimeController,
)

from services.intelligence.runtime.task import Task



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test": True
        }
    )



def test_controller_init():

    controller = RuntimeController()

    assert (
        controller.initialized
        is False
    )



def test_initialize():

    controller = RuntimeController()

    controller.initialize()

    assert (
        controller.initialized
        is True
    )



def test_shutdown():

    controller = RuntimeController()

    controller.initialize()

    controller.shutdown()

    assert (
        controller.initialized
        is False
    )



def test_submit():

    controller = RuntimeController()

    controller.submit(
        create_task()
    )

    assert (
        controller.manager.pipeline.size()
        ==
        1
    )



def test_execute():

    controller = RuntimeController()

    controller.register(
        "analysis",
        lambda task: "success"
    )


    result = controller.execute(
        create_task()
    )


    assert (
        result.success
        is True
    )



def test_status():

    controller = RuntimeController()

    result = controller.status()

    assert "initialized" in result

    assert "runtime" in result