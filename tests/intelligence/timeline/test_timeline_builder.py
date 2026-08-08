from services.intelligence.timeline.timeline_builder import (
    TimelineBuilder,
)



def test_timeline_builder():

    builder = TimelineBuilder()


    result = builder.build(

        [
            {
                "type": "alert",
                "description": "Phishing detected",
                "source": "email_engine",
            }
        ]

    )


    assert len(result) == 1

    assert result[0].event_type == "alert"