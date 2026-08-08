"""
Sentinel DNA Timeline Engine

Provides investigation history generation.
"""

from __future__ import annotations

from typing import Any

from .timeline_builder import TimelineBuilder



class TimelineEngine:
    """
    Enterprise timeline processor.
    """


    def __init__(self):

        self.builder = TimelineBuilder()



    def generate(
        self,
        events: list[Any],
    ) -> list[dict]:

        timeline = (
            self.builder.build(
                events
            )
        )


        return [

            item.to_dict()

            for item in timeline

        ]