"""
Sentinel DNA Runtime Intelligence Router

Canonical capability and agent routing layer.

Responsibilities
----------------
- Register intelligence capability handlers.
- Register runtime agents.
- Route intelligence requests.
- Preserve runtime context objects.
- Fall back to runtime agents when no direct handler exists.
- Maintain lightweight routing metrics.
- Provide a stable runtime status contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .runtime_agent.runtime_agent_orchestrator import (
    RuntimeAgentOrchestrator,
)
from .task import Task


RuntimeHandler = Callable[[Any], Any]


@dataclass
class RuntimeIntelligenceRouter:
    """
    Routes intelligence execution requests.

    The router deliberately preserves the payload object passed to
    registered handlers. This is important because intelligence
    execution may use a domain context object such as
    ``RuntimeIntelligenceContext`` rather than a plain dictionary.

    Supported routing forms
    ------------------------
    1. ``route(Task)``
    2. ``route(capability, payload)``

    Capability handlers receive the payload exactly as supplied.

    Runtime agents receive a ``Task`` whose payload is normalized to
    a dictionary when possible.
    """

    orchestrator: RuntimeAgentOrchestrator = field(
        default_factory=RuntimeAgentOrchestrator
    )

    handlers: dict[str, RuntimeHandler] = field(
        default_factory=dict
    )

    routes: int = 0

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register_agent(
        self,
        agent: Any,
    ) -> None:
        """
        Register a runtime agent.

        Parameters
        ----------
        agent:
            Runtime agent instance.
        """

        self.orchestrator.register_agent(agent)

    def register(
        self,
        capability: Any,
        handler: RuntimeHandler | None = None,
    ) -> None:
        """
        Register either an agent or a capability handler.

        Supported forms
        ----------------
        ``register(agent)``

        or:

        ``register(capability, handler)``
        """

        # --------------------------------------------------------------
        # Agent registration
        # --------------------------------------------------------------

        if handler is None:
            self.register_agent(capability)
            return

        # --------------------------------------------------------------
        # Capability validation
        # --------------------------------------------------------------

        if not isinstance(capability, str):
            raise TypeError(
                "Capability route must use a string capability."
            )

        normalized_capability = capability.strip()

        if not normalized_capability:
            raise ValueError(
                "Capability route cannot be empty."
            )

        if not callable(handler):
            raise TypeError(
                "Route handler must be callable."
            )

        # --------------------------------------------------------------
        # Handler registration
        # --------------------------------------------------------------

        self.handlers[normalized_capability] = handler

    # ------------------------------------------------------------------
    # Availability
    # ------------------------------------------------------------------

    def available(
        self,
        capability: str,
    ) -> bool:
        """
        Check whether a capability is available.

        A capability is available when either:

        - a direct handler is registered, or
        - a runtime agent advertises the capability.
        """

        normalized_capability = str(
            capability
        ).strip()

        if not normalized_capability:
            return False

        if normalized_capability in self.handlers:
            return True

        return self.orchestrator.has_capability(
            normalized_capability
        )

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------

    def route(
        self,
        capability_or_task: Any,
        payload: Any = None,
    ) -> Any:
        """
        Route intelligence execution.

        Supported forms
        ----------------

        Task routing::

            route(Task(...))

        Capability routing::

            route(
                "investigation",
                RuntimeIntelligenceContext(...),
            )

        The payload passed to a registered capability handler is
        preserved exactly as supplied.

        This is intentional. Runtime domain objects such as
        ``RuntimeIntelligenceContext`` must not be converted into
        dictionaries because handlers may depend on their attributes
        and behavior.
        """

        # --------------------------------------------------------------
        # Task routing
        # --------------------------------------------------------------

        if isinstance(
            capability_or_task,
            Task,
        ):
            result = self.orchestrator.execute(
                capability_or_task
            )

            self.routes += 1

            return result

        # --------------------------------------------------------------
        # Capability normalization
        # --------------------------------------------------------------

        capability = str(
            capability_or_task
        ).strip()

        if not capability:
            return None

        # --------------------------------------------------------------
        # Direct handler routing
        # --------------------------------------------------------------

        handler = self.handlers.get(
            capability
        )

        if handler is not None:
            result = handler(payload)

            self.routes += 1

            return result

        # --------------------------------------------------------------
        # Runtime agent fallback
        # --------------------------------------------------------------

        if self.orchestrator.has_capability(
            capability
        ):
            task_payload = self._task_payload(
                payload
            )

            task = Task(
                capability=capability,
                payload=task_payload,
            )

            result = self.orchestrator.execute(
                task
            )

            self.routes += 1

            return result

        # --------------------------------------------------------------
        # Missing capability
        # --------------------------------------------------------------

        return None

    # ------------------------------------------------------------------
    # Payload normalization
    # ------------------------------------------------------------------

    @staticmethod
    def _task_payload(
        payload: Any,
    ) -> dict[str, Any]:
        """
        Normalize a payload for ``Task`` construction.

        Registered handlers receive the original payload object.

        Runtime agents, however, operate through ``Task`` and therefore
        require a dictionary payload.

        Dictionaries are copied to prevent accidental mutation of the
        caller's dictionary.

        Objects exposing a ``to_dict()`` method are converted through
        that explicit domain contract.

        Otherwise a small, safe representation is created for the task
        payload.
        """

        if payload is None:
            return {}

        if isinstance(payload, dict):
            return dict(payload)

        to_dict = getattr(
            payload,
            "to_dict",
            None,
        )

        if callable(to_dict):
            converted = to_dict()

            if isinstance(converted, dict):
                return dict(converted)

        # Runtime contexts may not expose to_dict(). Preserve the most
        # useful common fields without forcing domain objects to become
        # mappings.
        fields = (
            "investigation_id",
            "evidence",
            "iocs",
            "mitre",
            "metadata",
        )

        extracted: dict[str, Any] = {}

        for field_name in fields:
            if hasattr(payload, field_name):
                extracted[field_name] = getattr(
                    payload,
                    field_name,
                )

        if extracted:
            return extracted

        return {
            "value": payload,
        }

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Clear routing state.
        """

        self.handlers.clear()

        self.orchestrator.clear()

        self.routes = 0

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return router runtime status.
        """

        return {
            "routes": self.routes,
            "handlers": list(
                self.handlers.keys()
            ),
            "agents": self.orchestrator.agent_count(),
            "orchestrator": self.orchestrator.status(),
        }