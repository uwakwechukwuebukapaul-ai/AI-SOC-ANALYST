"""
Sentinel DNA Runtime Dependency Manager

Manages runtime component dependencies.

Responsibilities:

- Register dependencies
- Validate availability
- Track dependency status
- Provide dependency snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Dependency:
    """
    Runtime dependency definition.
    """

    name: str

    checker: Callable[[], bool] | None = None

    required: bool = True

    status: str = "unknown"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class DependencyManager:
    """
    Enterprise dependency registry.
    """

    def __init__(self):

        self.dependencies: dict[str, Dependency] = {}



    def register(
        self,
        name: str,
        checker: Callable[[], bool] | None = None,
        required: bool = True,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Register runtime dependency.
        """

        self.dependencies[name] = Dependency(
            name=name,
            checker=checker,
            required=required,
            metadata=metadata or {},
        )



    def check(
        self,
        name: str,
    ) -> bool:
        """
        Validate dependency.
        """

        dependency = self.dependencies.get(
            name
        )

        if dependency is None:
            return False


        if dependency.checker is None:

            dependency.status = "available"

            return True


        try:

            result = dependency.checker()

            dependency.status = (
                "available"
                if result
                else "unavailable"
            )

            return result


        except Exception:

            dependency.status = "error"

            return False



    def check_all(self) -> bool:
        """
        Validate all dependencies.
        """

        result = True

        for name in self.dependencies:

            valid = self.check(name)

            dependency = self.dependencies[name]

            if dependency.required and not valid:
                result = False


        return result



    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove dependency.
        """

        self.dependencies.pop(
            name,
            None,
        )



    def clear(self) -> None:
        """
        Clear registry.
        """

        self.dependencies.clear()



    def status(self) -> dict[str, Any]:
        """
        Dependency snapshot.
        """

        return {
            name: {
                "status": dependency.status,
                "required": dependency.required,
                "metadata": dependency.metadata,
            }
            for name, dependency
            in self.dependencies.items()
        }



    def to_dict(self) -> dict[str, Any]:
        return self.status()