"""
Sentinel DNA
Dashboard Route
"""

from pathlib import Path
import sys

from flask import render_template

# =====================================
# PROJECT PATH
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


# =====================================
# DATABASE
# =====================================

from database.repository import get_cases


# =====================================
# DASHBOARD
# =====================================

def dashboard():

    try:
        cases = get_cases()

    except Exception:
        cases = []

    stats = {

        "total_cases": len(cases),

        "open_cases": len(
            [c for c in cases if c.get("status") == "OPEN"]
        ),

        "closed_cases": len(
            [c for c in cases if c.get("status") == "CLOSED"]
        ),

        "high_cases": len(
            [c for c in cases if c.get("severity") == "HIGH"]
        ),

        "cases": cases

    }

    return render_template(
        "dashboard.html",
        stats=stats
    )