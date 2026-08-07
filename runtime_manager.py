"""
Sentinel DNA Runtime Manager

Controls Runtime Engine lifecycle.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .runtime_engine import RuntimeEngine


@dataclass
class RuntimeManager:
    """
    Runtime lifecycle controller.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    running: bool = False


    def start(self) -> None:
        """
        Start runtime.
        """

        self.running = True


    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.running = False


    def restart(self) -> None:
        """
        Restart runtime.
        """

        self.stop()
        self.start()


    def is_running(self) -> bool:
        """
        Runtime status.
        """

        return self.running


    def health(self) -> dict:

        return {
            "running": self.running,
            "engine": self.engine.status(),
        }