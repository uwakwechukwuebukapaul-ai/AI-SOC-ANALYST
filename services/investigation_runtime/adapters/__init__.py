"""
Investigation Runtime Service Adapters.

Provides a stable integration boundary between the
Investigation Runtime and Sentinel DNA intelligence services.
"""

from .service_adapter import ServiceAdapter
from .intelligence_adapter import IntelligenceServiceAdapter

__all__ = [
    "ServiceAdapter",
    "IntelligenceServiceAdapter",
]