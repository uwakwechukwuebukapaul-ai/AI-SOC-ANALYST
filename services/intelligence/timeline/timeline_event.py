"""
Timeline Event Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class TimelineEvent:
    """
    Represents a single investigation event.
    """

    event_type: str

    description: str

    source: str

    timestamp: str | None = None


    def __post_init__(self):

        if self.timestamp is None:

            self.timestamp = (
                datetime.now(
                    timezone.utc
                )
                .isoformat()
            )


    def to_dict(self) -> dict:

        return {
            "event_type": self.event_type,
            "description": self.description,
            "source": self.source,
            "timestamp": self.timestamp,
        }