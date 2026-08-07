"""
Runtime Control Plane Tests
"""

from services.intelligence.runtime.runtime_control_plane import (
    RuntimeControlPlane,
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


    plane.submit(
        "analysis",
        {
            "id": 1
        },
    )


    assert (
        plane.execution.pending()
        ==
        1
    )


def test_status():

    plane = RuntimeControlPlane()


    result = plane.status()


    assert "running" in result

    assert "execution" in result

    assert "security" in result