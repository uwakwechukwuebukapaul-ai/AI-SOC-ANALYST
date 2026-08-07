"""
Sentinel DNA Runtime Controller

Control plane for Intelligence Runtime.

Responsibilities:

- Runtime startup/shutdown
- Component coordination
- Runtime state management
- Worker orchestration
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_engine import RuntimeEngine
from .runtime_state import RuntimeStateManager
from .runtime_events import RuntimeEventBus


@dataclass
class RuntimeController:
    """
    Enterprise runtime control plane.
    """

    engine: RuntimeEngine = field(
        default_factory=RuntimeEngine
    )

    state: RuntimeStateManager = field(
        default_factory=RuntimeStateManager
    )

    events: RuntimeEventBus = field(
        default_factory=RuntimeEventBus
    )

    running: bool = False


    def start(self) -> None:
        """
        Start runtime.
        """

        self.running = True

        self.state.set_status(
            "running"
        )

        self.events.publish(
            "runtime.started"
        )


    def stop(self) -> None:
        """
        Stop runtime.
        """

        self.running = False

        self.state.set_status(
            "stopped"
        )

        self.events.publish(
            "runtime.stopped"
        )


    def restart(self) -> None:
        """
        Restart runtime.
        """

        self.stop()

        self.start()



    def health(self) -> dict[str, Any]:
        """
        Runtime health report.
        """

        return {
            "running":
                self.running,

            "state":
                self.state.get_status(),

            "engine":
                self.engine.status(),
        }



    def status(self) -> dict[str, Any]:
        """
        Runtime status snapshot.
        """

        return {
            "running":
                self.running,

            "state":
                self.state.snapshot(),

            "events":
                self.events.status(),

            "engine":
                self.engine.status(),
        }