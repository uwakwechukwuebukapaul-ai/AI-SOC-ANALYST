"""
Sentinel DNA Case Timeline

Tracks investigation events.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any


class CaseTimeline:
    """
    Investigation event timeline.
    """

    def __init__(self):

        self.events: list[dict[str, Any]] = []


    def add_event(
        self,
        event_type: str,
        description: str,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "type": event_type,
            "description": description,
            "metadata": metadata or {},
        }

        self.events.append(event)

        return event


    def get_events(self):

        return self.events