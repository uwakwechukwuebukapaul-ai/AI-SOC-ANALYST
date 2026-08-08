from services.intelligence.timeline.timeline_event import (
    TimelineEvent,
)



def test_timeline_event():

    event = TimelineEvent(
        event_type="ioc_detected",
        description="Malicious domain found",
        source="ioc_engine",
    )


    data = event.to_dict()


    assert data["event_type"] == "ioc_detected"

    assert data["source"] == "ioc_engine"

    assert data["timestamp"] is not None