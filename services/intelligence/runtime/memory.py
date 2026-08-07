"""
Sentinel DNA Runtime Memory

Shared runtime state storage
for Intelligence agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeMemory:
    """
    Shared key-value runtime memory.
    """

    storage: dict[str, Any] = field(
        default_factory=dict
    )


    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store value.
        """

        self.storage[key] = value



    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve value.
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
        Check key existence.
        """

        return key in self.storage



    def delete(
        self,
        key: str,
    ) -> bool:
        """
        Remove value.
        """

        if key in self.storage:

            del self.storage[key]

            return True


        return False



    def clear(self) -> None:
        """
        Remove all memory.
        """

        self.storage.clear()



    def size(self) -> int:
        """
        Number of stored values.
        """

        return len(self.storage)



    def snapshot(self) -> dict[str, Any]:
        """
        Return memory copy.
        """

        return dict(
            self.storage
        )



    def to_dict(self) -> dict[str, Any]:
        """
        Export memory state.
        """

        return {
            "size": self.size(),
            "memory": self.snapshot(),
        }