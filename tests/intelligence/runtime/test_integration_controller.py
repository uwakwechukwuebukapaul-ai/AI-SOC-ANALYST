from services.intelligence.runtime.integration_controller import (
    RuntimeIntegrationController
)


def test_controller_init():

    controller = RuntimeIntegrationController()

    assert controller.engine is not None



def test_start():

    controller = RuntimeIntegrationController()

    controller.start()

    assert controller.state.status == "running"



def test_stop():

    controller = RuntimeIntegrationController()

    controller.stop()

    assert controller.state.status == "stopped"



def test_submit():

    controller = RuntimeIntegrationController()

    assert controller.submit is not None



def test_status():

    controller = RuntimeIntegrationController()

    data = controller.status()

    assert "state" in data
    assert "engine" in data