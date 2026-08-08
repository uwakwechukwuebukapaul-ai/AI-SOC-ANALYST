"""
Sentinel DNA Evidence Artifact

Canonical representation of investigation evidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass
class Artifact:
    """
    Investigation evidence object.
    """

    artifact_id: str

    artifact_type: str

    value: Any

    source: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
            datetime.now(
                UTC
            ).isoformat()
    )


    def to_dict(self) -> dict[str, Any]:

        return {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "value": self.value,
            "source": self.source,
            "metadata": self.metadata,
            "created_at": self.created_at,
        }