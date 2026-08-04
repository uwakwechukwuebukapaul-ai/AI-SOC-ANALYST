"""
Sentinel DNA
Enterprise Investigation Audit Logger

Provides immutable audit events for investigation lifecycle tracking.

Author: Sentinel DNA
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def utc_now() -> datetime:
    """
    Returns timezone-aware UTC datetime.
    """
    return datetime.now(timezone.utc)


@dataclass
class AuditEvent:
    """
    Represents a single investigation audit event.
    """

    stage: str

    event_type: str

    message: str

    investigation_id: Optional[str] = None

    case_id: Optional[int] = None

    timestamp: str = ""


class AuditLogger:
    """
    Enterprise audit event collector.

    Future expansion:
    - Database persistence
    - SIEM forwarding
    - Compliance reporting
    - Immutable event storage
    """

    def __init__(self):
        self.events: List[AuditEvent] = []


    def log_event(
        self,
        stage: str,
        event_type: str,
        message: str,
        investigation_id: Optional[str] = None,
        case_id: Optional[int] = None,
    ) -> AuditEvent:
        """
        Create and store an audit event.
        """

        event = AuditEvent(
            stage=stage,
            event_type=event_type,
            message=message,
            investigation_id=investigation_id,
            case_id=case_id,
            timestamp=utc_now().isoformat(),
        )

        self.events.append(event)

        return event


    def get_events(self) -> List[Dict[str, Any]]:
        """
        Return serialized audit events.
        """

        return [
            asdict(event)
            for event in self.events
        ]


    def clear(self) -> None:
        """
        Clear audit history.

        Mainly used for testing.
        """

        self.events.clear()


# Global audit logger instance
audit_logger = AuditLogger()