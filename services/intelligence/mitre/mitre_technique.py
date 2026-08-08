"""
Sentinel DNA MITRE Technique Model
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class MitreTechnique:
    """
    Represents MITRE ATT&CK technique.
    """

    technique_id: str

    name: str

    tactic: str

    description: str = ""

    metadata: dict[str, Any] | None = None


    def to_dict(self):

        return {
            "technique_id": self.technique_id,
            "name": self.name,
            "tactic": self.tactic,
            "description": self.description,
            "metadata": self.metadata or {},
        }