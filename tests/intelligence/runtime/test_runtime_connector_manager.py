"""
Runtime Connector Manager Tests
"""

from services.intelligence.runtime.runtime_connector_manager import (
    RuntimeConnectorManager,
)



def test_init():

    manager = RuntimeConnectorManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimeConnectorManager()


    manager.register(
        "splunk",
        {
            "type":
                "siem"
        },
    )


    assert (
        manager.available(
            "splunk"
        )
        is True
    )



def test_disconnect():

    manager = RuntimeConnectorManager()


    manager.register(
        "crowdstrike",
        {},
    )


    manager.disconnect(
        "crowdstrike"
    )


    assert (
        manager.available(
            "crowdstrike"
        )
        is False
    )



def test_connect():

    manager = RuntimeConnectorManager()


    manager.register(
        "elastic",
        {},
    )


    manager.disconnect(
        "elastic"
    )

    manager.connect(
        "elastic"
    )


    assert (
        manager.available(
            "elastic"
        )
        is True
    )



def test_remove():

    manager = RuntimeConnectorManager()


    manager.register(
        "test",
        {},
    )


    manager.remove(
        "test"
    )


    assert (
        manager.available(
            "test"
        )
        is False
    )



def test_clear():

    manager = RuntimeConnectorManager()


    manager.register(
        "test",
        {},
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeConnectorManager()


    result = manager.status()


    assert "connectors" in result

    assert "count" in result