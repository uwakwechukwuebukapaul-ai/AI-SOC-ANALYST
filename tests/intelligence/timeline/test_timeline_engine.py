from services.intelligence.timeline.timeline_engine import (
    TimelineEngine,
)



def test_timeline_engine():

    engine = TimelineEngine()


    result = engine.generate(

        [

            {
                "type": "investigation_started",
                "description": "Case opened",
                "source": "coordinator",
            }

        ]

    )


    assert len(result) == 1

    assert (
        result[0]["event_type"]
        ==
        "investigation_started"
    )