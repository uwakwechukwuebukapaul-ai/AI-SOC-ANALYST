from services.intelligence.cases.case_timeline import (
    CaseTimeline,
)


def test_timeline_event():

    timeline = CaseTimeline()

    event = timeline.add_event(
        "ioc_found",
        "Malicious domain detected",
    )


    assert event["type"] == "ioc_found"

    assert len(
        timeline.get_events()
    ) == 1