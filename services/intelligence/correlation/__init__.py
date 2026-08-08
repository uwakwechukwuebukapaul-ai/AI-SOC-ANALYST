"""
Sentinel DNA Evidence Correlation Layer
"""

from .correlation_engine import (
    CorrelationEngine,
)

from .finding_correlator import (
    FindingCorrelator,
)


__all__ = [
    "CorrelationEngine",
    "FindingCorrelator",
]