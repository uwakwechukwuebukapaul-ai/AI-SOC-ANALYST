"""
Default Sentinel DNA investigation runtime providers.

This package exposes the production service-provider composition
used by the Investigation Runtime.
"""

from .default_providers import (
    create_default_service_bridge,
    register_default_services,
)

__all__ = [
    "create_default_service_bridge",
    "register_default_services",
]