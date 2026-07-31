"""
Sentinel DNA
Enterprise Investigation Audit Logger

Provides centralized audit logging for investigation events.

Author: Sentinel DNA
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional


LOGGER_NAME = "sentinel_dna.orchestrator.audit"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


logger = logging.getLogger(LOGGER_NAME)


@dataclass
class AuditEvent:
    """
    Represents a single audit event generated during an
    investigation.
    """

    timestamp: str

    stage: str

    event_type: str

    message: str

    investigation_id: Optional[str] = None

    case_id: Optional[int] = None

    actor: str = "SYSTEM"

    metadata: Optional[Dict[str, Any]] = None


class AuditLogger:
    """
    Centralized audit logger.

    Stores audit events in memory for the current
    investigation and writes them to the application log.

    Future versions can persist these events to SQLite,
    Elasticsearch, Splunk, Microsoft Sentinel,
    or other SIEM platforms.
    """

    def __init__(self):
        self.events: List[AuditEvent] = []

    def log_event(
        self,
        *,
        stage: str,
        event_type: str,
        message: str,
        investigation_id: Optional[str] = None,
        case_id: Optional[int] = None,
        actor: str = "SYSTEM",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> AuditEvent:

        event = AuditEvent(
            timestamp=datetime.utcnow().isoformat(),
            stage=stage,
            event_type=event_type,
            message=message,
            investigation_id=investigation_id,
            case_id=case_id,
            actor=actor,
            metadata=metadata or {},
        )

        self.events.append(event)

        logger.info(
            "[%s] %s | %s",
            event.stage,
            event.event_type,
            event.message,
        )

        return event

    def get_events(self) -> List[Dict[str, Any]]:
        """
        Return all audit events as dictionaries.
        """
        return [asdict(event) for event in self.events]

    def clear(self) -> None:
        """
        Clear the current audit session.
        """
        self.events.clear()

    def count(self) -> int:
        """
        Return total number of audit events.
        """
        return len(self.events)


audit_logger = AuditLogger()