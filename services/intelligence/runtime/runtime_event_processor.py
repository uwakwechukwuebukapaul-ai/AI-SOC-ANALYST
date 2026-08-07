"""
Sentinel DNA Runtime Event Processor

Event processing execution layer.

Responsibilities:

- register event processors
- consume runtime events
- execute handlers
- track processing metrics
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeEventProcessor:
    """
    Runtime event processing engine.
    """

    processors: dict[str, list[Callable]] = field(
        default_factory=dict
    )

    processed: int = 0


    def register(
        self,
        event_type: str,
        processor: Callable,
    ) -> None:
        """
        Register event processor.
        """

        if event_type not in self.processors:
            self.processors[event_type] = []

        self.processors[event_type].append(
            processor
        )



    def process(
        self,
        event_type: str,
        payload: dict[str, Any],
    ) -> list[Any]:
        """
        Process runtime event.
        """

        results = []


        for processor in self.processors.get(
            event_type,
            [],
        ):
            results.append(
                processor(payload)
            )

            self.processed += 1


        return results



    def processor_count(
        self,
        event_type: str,
    ) -> int:
        """
        Return processor count.
        """

        return len(
            self.processors.get(
                event_type,
                [],
            )
        )



    def clear(self) -> None:
        """
        Reset processors.
        """

        self.processors.clear()

        self.processed = 0



    def status(self) -> dict[str, Any]:
        """
        Processor status.
        """

        return {
            "processed":
                self.processed,

            "processors":
                sum(
                    len(items)
                    for items in self.processors.values()
                ),
        }