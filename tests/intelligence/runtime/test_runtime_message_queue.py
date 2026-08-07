"""
Runtime Message Queue Tests
"""

from services.intelligence.runtime.runtime_message_queue import (
    RuntimeMessageQueue,
)



def test_init():

    queue = RuntimeMessageQueue()

    assert (
        queue.size()
        ==
        0
    )



def test_publish():

    queue = RuntimeMessageQueue()


    queue.publish(
        "incident",
        {
            "id":
                "INC001"
        },
    )


    assert (
        queue.size()
        ==
        1
    )



def test_consume():

    queue = RuntimeMessageQueue()


    queue.publish(
        "alert",
        {},
    )


    result = queue.consume()


    assert (
        result["topic"]
        ==
        "alert"
    )



def test_empty_consume():

    queue = RuntimeMessageQueue()


    result = queue.consume()


    assert result is None



def test_processed_count():

    queue = RuntimeMessageQueue()


    queue.publish(
        "event",
        {},
    )


    queue.consume()


    assert (
        queue.count()
        ==
        1
    )



def test_clear():

    queue = RuntimeMessageQueue()


    queue.publish(
        "test",
        {},
    )


    queue.clear()


    assert (
        queue.size()
        ==
        0
    )



def test_status():

    queue = RuntimeMessageQueue()


    result = queue.status()


    assert "queue_size" in result

    assert "processed" in result