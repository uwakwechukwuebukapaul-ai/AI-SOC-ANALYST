"""
Sentinel DNA Runtime Bootstrap

Application startup initializer.

Responsibilities:

- initialize intelligence runtime
- register default capabilities
- expose runtime instance
"""

from __future__ import annotations

from typing import Callable

from .runtime_intelligence_runtime import (
    RuntimeIntelligenceRuntime,
)


_runtime: RuntimeIntelligenceRuntime | None = None



def initialize_runtime() -> RuntimeIntelligenceRuntime:
    """
    Initialize Sentinel DNA intelligence runtime.
    """

    global _runtime


    if _runtime is None:

        _runtime = RuntimeIntelligenceRuntime()

        _runtime.start()


    return _runtime



def get_runtime() -> RuntimeIntelligenceRuntime:
    """
    Get active runtime instance.
    """

    if _runtime is None:
        return initialize_runtime()


    return _runtime



def register_capability(
    capability: str,
    handler: Callable,
) -> None:
    """
    Register runtime capability.
    """

    runtime = get_runtime()


    runtime.register(
        capability,
        handler,
    )