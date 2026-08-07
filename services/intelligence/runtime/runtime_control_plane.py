"""
Sentinel DNA Runtime Control Plane

Enterprise runtime coordination layer.

Responsibilities:

- runtime lifecycle control
- execution delegation
- event management
- health monitoring
- workflow compatibility
"""

from __future__ import annotations

from typing import Any

from .runtime_execution_manager import (
    RuntimeExecutionManager,
)

from .runtime_health_monitor import (
    RuntimeHealthMonitor,
)

from .task import Task


class RuntimeEventBus:
    """
    Runtime event dispatcher.
    """

    def __init__(self):

        self.handlers = {}


    def register(
        self,
        name: str,
        handler,
    ) -> None:
        """
        Register event handler.
        """

        self.handlers[name] = handler


    def emit(
        self,
        name: str,
        payload: dict[str, Any],
    ) -> None:
        """
        Emit runtime event.
        """

        handler = self.handlers.get(
            name
        )

        if handler:
            handler(payload)


    def status(self) -> dict[str, Any]:
        """
        Event status.
        """

        return {
            "registered":
                len(self.handlers),

            "events":
                list(self.handlers.keys()),
        }



class RuntimeControlPlane:
    """
    Controls runtime execution.
    """

    def __init__(self):

        self.runtime = RuntimeExecutionManager()

        self.health = RuntimeHealthMonitor()

        self.events = RuntimeEventBus()

        self.running = False

        self.last_task = None


        # compatibility alias

        self.execution = self.runtime



    def start(self):

        self.running = True

        self.runtime.start()



    def stop(self):

        self.running = False

        self.runtime.stop()



    def submit(
        self,
        task,
        payload=None,
    ):
        """
        Submit runtime task.

        Supports:

        submit(Task)
        submit(Task,payload)
        submit(capability,payload)
        """

        if isinstance(task, str):

            task = Task(
                capability=task,
                payload=payload or {},
            )


        elif payload is not None:

            task.payload = payload


        self.last_task = task


        return self.runtime.submit(
            task
        )



    def execute(
        self,
        task=None,
    ):
        """
        Execute runtime task.

        Supports:

        execute(Task)

        execute()
        using last submitted workflow
        """

        if task is None:

            task = self.last_task


        if task is None:

            return None


        return self.runtime.execute(
            task
        )



    def emit(
        self,
        name,
        payload,
    ):

        self.events.emit(
            name,
            payload
        )



    def status(self):

        return {

            "running":
                self.running,


            "execution":
                self.runtime.status(),


            "runtime":
                self.runtime.status(),


            "health":
                self.health.check(),


            "events":
                self.events.status(),

        }