"""
Sentinel DNA Runtime Store

Persistence layer for runtime state,
task snapshots, and execution recovery.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import copy


@dataclass
class RuntimeStore:
    """
    Runtime persistence manager.
    """

    storage: dict[str, Any] = field(
        default_factory=dict
    )

    snapshots: dict[str, dict] = field(
        default_factory=dict
    )


    def save(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Save runtime data.
        """

        self.storage[key] = value



    def load(
        self,
        key: str,
        default=None,
    ) -> Any:
        """
        Load runtime data.
        """

        return self.storage.get(
            key,
            default,
        )



    def exists(
        self,
        key: str,
    ) -> bool:
        """
        Check stored value.
        """

        return key in self.storage



    def delete(
        self,
        key: str,
    ) -> None:
        """
        Remove stored value.
        """

        self.storage.pop(
            key,
            None,
        )



    def snapshot(
        self,
        name: str,
    ) -> dict:
        """
        Create runtime snapshot.
        """

        snapshot = copy.deepcopy(
            self.storage
        )

        self.snapshots[name] = snapshot

        return snapshot



    def restore(
        self,
        name: str,
    ) -> dict:
        """
        Restore runtime snapshot.
        """

        snapshot = self.snapshots.get(
            name,
            {},
        )

        self.storage = copy.deepcopy(
            snapshot
        )

        return self.storage



    def clear(self) -> None:
        """
        Clear runtime storage.
        """

        self.storage.clear()



    def to_dict(self) -> dict:
        """
        Export runtime state.
        """

        return {
            "storage":
                self.storage,

            "snapshots":
                list(
                    self.snapshots.keys()
                ),
        }