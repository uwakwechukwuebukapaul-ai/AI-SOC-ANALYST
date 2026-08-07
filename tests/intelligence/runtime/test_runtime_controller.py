from services.intelligence.runtime.runtime_controller import (
    RuntimeController,
)



def test_controller_init():

    controller = RuntimeController()

    assert (
        controller.running
        is False
    )



def test_start():

    controller = RuntimeController()

    controller.start()

    assert (
        controller.running
        is True
    )

    assert (
        controller.state.get_status()
        ==
        "running"
    )



def test_stop():

    controller = RuntimeController()

    controller.start()

    controller.stop()

    assert (
        controller.running
        is False
    )

    assert (
        controller.state.get_status()
        ==
        "stopped"
    )



def test_restart():

    controller = RuntimeController()

    controller.start()

    controller.restart()

    assert (
        controller.running
        is True
    )



def test_health():

    controller = RuntimeController()

    result = controller.health()

    assert "running" in result

    assert "state" in result



def test_status():

    controller = RuntimeController()

    result = controller.status()

    assert "engine" in result

    assert "events" in result