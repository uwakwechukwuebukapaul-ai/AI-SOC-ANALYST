"""
Runtime Control Plane Tests
"""

from services.intelligence.runtime.runtime_control_plane import (
    RuntimeControlPlane,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

    plane = RuntimeControlPlane()

    assert (
        plane.running
        is False
    )



def test_start():

    plane = RuntimeControlPlane()


    plane.start()


    assert (
        plane.running
        is True
    )



def test_stop():

    plane = RuntimeControlPlane()


    plane.start()

    plane.stop()


    assert (
        plane.running
        is False
    )



def test_submit():

    plane = RuntimeControlPlane()


    plane.start()


    plane.execution.workers.executor.register(
        "analysis",
        lambda data: {
            "ok":
                True
        },
    )


    result = plane.submit(
        create_task()
    )


    assert (
        result["ok"]
        is True
    )



def test_event():

    plane = RuntimeControlPlane()


    result = []


    plane.events.register(
        "alert",
        lambda data: result.append(data),
    )


    plane.emit(
        "alert",
        {
            "level":
                "high"
        },
    )


    assert (
        result[0]["level"]
        ==
        "high"
    )



def test_status():

    plane = RuntimeControlPlane()


    result = plane.status()


    assert "running" in result

    assert "execution" in result

    assert "events" in result

    assert "health" in result