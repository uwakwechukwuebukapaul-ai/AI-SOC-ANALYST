"""
Sentinel DNA Runtime Hooks

Extension point system for runtime automation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimeHook:
    """
    Runtime execution hook.
    """

    name: str

    callback: Callable

    enabled: bool = True

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def execute(
        self,
        *args,
        **kwargs,
    ):
        """
        Execute hook callback.
        """

        if not self.enabled:
            return None

        return self.callback(
            *args,
            **kwargs
        )



class RuntimeHookManager:
    """
    Runtime hook registry.
    """

    def __init__(self):

        self.hooks: dict[
            str,
            RuntimeHook
        ] = {}



    def register(
        self,
        hook: RuntimeHook,
    ) -> None:
        """
        Register runtime hook.
        """

        self.hooks[hook.name] = hook



    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove hook.
        """

        self.hooks.pop(
            name,
            None,
        )



    def execute(
        self,
        name: str,
        *args,
        **kwargs,
    ):
        """
        Execute registered hook.
        """

        hook = self.hooks.get(name)

        if not hook:
            return None


        return hook.execute(
            *args,
            **kwargs
        )



    def enable(
        self,
        name: str,
    ) -> None:

        if name in self.hooks:
            self.hooks[name].enabled = True



    def disable(
        self,
        name: str,
    ) -> None:

        if name in self.hooks:
            self.hooks[name].enabled = False



    def clear(self) -> None:
        """
        Remove all hooks.
        """

        self.hooks.clear()



    def to_dict(self) -> dict[str, Any]:
        """
        Export hooks.
        """

        return {
            "hooks": [
                {
                    "name": hook.name,
                    "enabled": hook.enabled,
                    "metadata": hook.metadata,
                }
                for hook in self.hooks.values()
            ]
        }