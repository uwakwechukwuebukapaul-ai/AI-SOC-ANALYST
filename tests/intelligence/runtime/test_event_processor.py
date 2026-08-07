from services.intelligence.runtime.event_processor import (
    EventProcessor,
)


def test_processor_init():

    processor = EventProcessor()

    assert processor.enabled is True



def test_register_event():

    processor = EventProcessor()

    def handler(data):
        return data


    processor.register(
        "test",
        handler,
    )

    assert "test" in processor.handlers



def test_process_event():

    processor = EventProcessor()

    processor.register(
        "test",
        lambda x: x + 1,
    )


    result = processor.process(
        "test",
        5,
    )


    assert result[0] == 6

    assert processor.processed_events == 1



def test_remove_event():

    processor = EventProcessor()


    def handler(data):
        return data


    processor.register(
        "test",
        handler,
    )


    processor.remove(
        "test",
        handler,
    )


    assert handler not in processor.handlers["test"]



def test_status():

    processor = EventProcessor()


    data = processor.status()


    assert "events" in data

    assert "processed_events" in data