"""
Sentinel DNA Timeline Repository

Stores chronological investigation events.
"""

from __future__ import annotations

from datetime import datetime, timezone

from typing import Any


class TimelineRepository:
    """
    Investigation timeline storage.
    """

    def __init__(self) -> None:

        self._events: dict[
            str,
            list[dict[str, Any]],
        ] = {}



    # --------------------------------------------------
    # Add event
    # --------------------------------------------------

    def add_event(
        self,
        case_id: str,
        event: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Add timeline event.
        """

        event = {
            **event,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
        }


        if case_id not in self._events:

            self._events[case_id] = []


        self._events[case_id].append(
            event
        )


        return event



    # --------------------------------------------------
    # Get timeline
    # --------------------------------------------------

    def get_events(
        self,
        case_id: str,
    ) -> list[dict[str, Any]]:

        return self._events.get(
            case_id,
            [],
        )



    # --------------------------------------------------
    # Clear timeline
    # --------------------------------------------------

    def delete(
        self,
        case_id: str,
    ) -> bool:

        if case_id in self._events:

            del self._events[case_id]

            return True


        return False