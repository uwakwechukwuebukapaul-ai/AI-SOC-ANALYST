"""
Investigation runtime persistence layer.

Provides repository abstractions and SQLite-backed
persistence for investigation state.
"""

from .investigation_repository import (
    InvestigationRepository,
)
from .sqlite_investigation_repository import (
    SQLiteInvestigationRepository,
)

__all__ = [
    "InvestigationRepository",
    "SQLiteInvestigationRepository",
]