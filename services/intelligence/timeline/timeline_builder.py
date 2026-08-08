"""
Timeline Builder

Creates investigation timelines.
"""

from __future__ import annotations

from typing import Any

from .timeline_event import TimelineEvent



class TimelineBuilder:
    """
    Builds ordered investigation events.
    """


    def build(
        self,
        events: list[Any],
    ) -> list[TimelineEvent]:

        timeline = []


        for event in events:

            if isinstance(
                event,
                TimelineEvent,
            ):

                timeline.append(event)

                continue


            timeline.append(

                TimelineEvent(

                    event_type=
                        event.get(
                            "type",
                            "unknown",
                        ),

                    description=
                        event.get(
                            "description",
                            "",
                        ),

                    source=
                        event.get(
                            "source",
                            "system",
                        ),

                )

            )


        return timeline