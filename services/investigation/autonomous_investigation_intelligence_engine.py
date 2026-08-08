"""
Autonomous Investigation Intelligence Engine.

Compatibility facade for the Sentinel DNA investigation service.

The canonical implementation lives in:

    services.investigation_runtime.
    autonomous_investigation_intelligence_engine

This module intentionally re-exports the canonical engine so existing
imports and integrations remain backward compatible while the runtime
implementation has a single source of truth.
"""

from __future__ import annotations

from services.investigation_runtime.autonomous_investigation_intelligence_engine import (
    AutonomousInvestigationIntelligenceEngine,
)

__all__ = [
    "AutonomousInvestigationIntelligenceEngine",
]