"""
Sentinel DNA Runtime Security Manager

Enterprise runtime security layer.

Responsibilities:

- register permissions
- validate access
- protect runtime operations
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any



@dataclass
class RuntimeSecurityManager:
    """
    Runtime access controller.
    """

    permissions: dict[str, set[str]] = field(
        default_factory=dict
    )



    def grant(
        self,
        identity: str,
        permission: str,
    ) -> None:
        """
        Grant permission.
        """

        if identity not in self.permissions:
            self.permissions[identity] = set()


        self.permissions[identity].add(
            permission
        )



    def revoke(
        self,
        identity: str,
        permission: str,
    ) -> None:
        """
        Revoke permission.
        """

        if identity in self.permissions:
            self.permissions[identity].discard(
                permission
            )



    def allowed(
        self,
        identity: str,
        permission: str,
    ) -> bool:
        """
        Check permission.
        """

        return permission in (
            self.permissions.get(
                identity,
                set(),
            )
        )



    def identity_exists(
        self,
        identity: str,
    ) -> bool:
        """
        Check identity registration.
        """

        return identity in self.permissions



    def remove(
        self,
        identity: str,
    ) -> None:
        """
        Remove identity permissions.
        """

        self.permissions.pop(
            identity,
            None,
        )



    def count(self) -> int:
        """
        Return identity count.
        """

        return len(
            self.permissions
        )



    def clear(self) -> None:
        """
        Reset permissions.
        """

        self.permissions.clear()



    def status(self) -> dict[str, Any]:
        """
        Security status.
        """

        return {
            "identities":
                self.permissions,

            "count":
                self.count(),
        }