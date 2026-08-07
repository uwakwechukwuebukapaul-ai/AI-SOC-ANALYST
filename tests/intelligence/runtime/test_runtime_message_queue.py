"""
Runtime Message Queue Tests
"""

from services.intelligence.runtime.runtime_message_queue import (
    RuntimeMessageQueue,
)



def test_queue_init():

    queue = RuntimeMessageQueue()

    assert (
        queue.size()
        ==
        0
    )



def test_enqueue():

    queue = RuntimeMessageQueue()


    queue.enqueue(
        {
            "event":
                "alert"
        }
    )


    assert (
        queue.size()
        ==
        1
    )



def test_dequeue():

    queue = RuntimeMessageQueue()


    message = {
        "id": 1
    }


    queue.enqueue(
        message
    )


    result = queue.dequeue()


    assert result == message



def test_peek():

    queue = RuntimeMessageQueue()


    queue.enqueue(
        {
            "task":
                "analysis"
        }
    )


    result = queue.peek()


    assert (
        result["task"]
        ==
        "analysis"
    )



def test_clear():

    queue = RuntimeMessageQueue()


    queue.enqueue(
        {}
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

    assert "empty" in result