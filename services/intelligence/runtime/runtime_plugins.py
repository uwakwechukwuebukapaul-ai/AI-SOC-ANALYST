"""
Sentinel DNA Runtime Plugins

Plugin registration and lifecycle management.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class RuntimePlugin:
    """
    Runtime extension plugin.
    """

    name: str

    version: str = "1.0.0"

    enabled: bool = True

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    start_handler: Callable | None = None

    stop_handler: Callable | None = None


    def start(self):
        """
        Start plugin.
        """

        if self.enabled and self.start_handler:
            return self.start_handler()



    def stop(self):
        """
        Stop plugin.
        """

        if self.stop_handler:
            return self.stop_handler()



class RuntimePluginManager:
    """
    Enterprise runtime plugin registry.
    """

    def __init__(self):

        self.plugins: dict[str, RuntimePlugin] = {}



    def register(
        self,
        plugin: RuntimePlugin,
    ) -> None:
        """
        Register plugin.
        """

        self.plugins[plugin.name] = plugin



    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove plugin.
        """

        self.plugins.pop(
            name,
            None,
        )



    def start_all(self):

        for plugin in self.plugins.values():
            plugin.start()



    def stop_all(self):

        for plugin in self.plugins.values():
            plugin.stop()



    def enable(
        self,
        name: str,
    ) -> None:

        if name in self.plugins:
            self.plugins[name].enabled = True



    def disable(
        self,
        name: str,
    ) -> None:

        if name in self.plugins:
            self.plugins[name].enabled = False



    def clear(self):

        self.plugins.clear()



    def to_dict(self) -> dict[str, Any]:

        return {
            "plugins": [
                {
                    "name": plugin.name,
                    "version": plugin.version,
                    "enabled": plugin.enabled,
                    "metadata": plugin.metadata,
                }
                for plugin in self.plugins.values()
            ]
        }