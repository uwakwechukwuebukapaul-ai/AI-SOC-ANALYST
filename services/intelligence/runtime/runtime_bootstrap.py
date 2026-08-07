"""
Sentinel DNA Runtime Bootstrap Service

Initializes the complete Intelligence Runtime Framework.

Startup order:

1. Configuration
2. Dependencies
3. State
4. Runtime Engine
5. Integration Controller
6. Runtime activation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_config import RuntimeConfig
from .dependency_manager import DependencyManager
from .runtime_state import RuntimeState
from .integration_controller import (
    RuntimeIntegrationController,
)



@dataclass
class RuntimeBootstrap:
    """
    Enterprise runtime initialization service.
    """

    config: RuntimeConfig = field(
        default_factory=RuntimeConfig
    )

    dependencies: DependencyManager = field(
        default_factory=DependencyManager
    )

    state: RuntimeState = field(
        default_factory=RuntimeState
    )

    controller: RuntimeIntegrationController = field(
        default_factory=RuntimeIntegrationController
    )

    initialized: bool = False



    def initialize(self) -> bool:
        """
        Initialize runtime stack.
        """

        dependency_status = (
            self.dependencies.check_all()
        )

        if not dependency_status:
            self.initialized = False
            return False


        self.state.start()

        self.controller.start()

        self.initialized = True

        return True



    def shutdown(self) -> None:
        """
        Shutdown runtime stack.
        """

        self.controller.stop()

        self.state.stop()

        self.initialized = False



    def register_dependency(
        self,
        name: str,
        checker=None,
        required: bool = True,
    ) -> None:
        """
        Register startup dependency.
        """

        self.dependencies.register(
            name,
            checker,
            required,
        )



    def status(self) -> dict[str, Any]:
        """
        Runtime bootstrap status.
        """

        return {
            "initialized": self.initialized,

            "config":
                self.config.to_dict(),

            "state":
                self.state.to_dict(),

            "controller":
                self.controller.status(),
        }