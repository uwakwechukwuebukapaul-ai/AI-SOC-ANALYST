"""
Runtime Event Processor Tests
"""

from services.intelligence.runtime.runtime_event_processor import (
    RuntimeEventProcessor,
)



def test_init():

    processor = RuntimeEventProcessor()

    assert (
        processor.processed
        ==
        0
    )



def test_register():

    processor = RuntimeEventProcessor()


    processor.register(
        "alert",
        lambda data: data,
    )


    assert (
        processor.processor_count(
            "alert"
        )
        ==
        1
    )



def test_process():

    processor = RuntimeEventProcessor()


    processor.register(
        "alert",
        lambda data: {
            "handled":
                True
        },
    )


    result = processor.process(
        "alert",
        {},
    )


    assert (
        result[0]["handled"]
        is True
    )



def test_processed_counter():

    processor = RuntimeEventProcessor()


    processor.register(
        "event",
        lambda data: True,
    )


    processor.process(
        "event",
        {},
    )


    assert (
        processor.processed
        ==
        1
    )



def test_clear():

    processor = RuntimeEventProcessor()


    processor.register(
        "event",
        lambda data: True,
    )


    processor.clear()


    assert (
        processor.processed
        ==
        0
    )



def test_status():

    processor = RuntimeEventProcessor()


    result = processor.status()


    assert "processed" in result

    assert "processors" in result