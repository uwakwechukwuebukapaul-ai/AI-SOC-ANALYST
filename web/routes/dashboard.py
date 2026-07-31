"""
Sentinel DNA
Dashboard Route

Provides:
- SOC dashboard statistics
- Analytics data
- Chart information
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
# IMPORTS
# =====================================

from database.repository import get_cases

from web.analytics.dashboard_stats import (
    get_dashboard_analytics
)





# =====================================
# DASHBOARD
# =====================================

def dashboard():


    try:

        cases = get_cases()


    except Exception:

        cases = []





    try:

        analytics = get_dashboard_analytics()


    except Exception:

        analytics = {

            "statistics": {},

            "severity": {},

            "status": {},

            "threats": {},

            "timeline": {},

            "risk": {}

        }







    stats = {


        "total_cases":

            analytics["statistics"].get(
                "total_cases",
                0
            ),



        "open_cases":

            analytics["statistics"].get(
                "open_cases",
                0
            ),



        "closed_cases":

            analytics["statistics"].get(
                "closed_cases",
                0
            ),



        "high_cases":

            analytics["statistics"].get(
                "high_cases",
                0
            ),



        "cases":

            cases

    }






    return render_template(

        "dashboard.html",

        stats=stats,


        analytics=analytics,


        severity_labels=list(
            analytics["severity"].keys()
        ),


        severity_values=list(
            analytics["severity"].values()
        ),



        threat_labels=list(
            analytics["threats"].keys()
        ),


        threat_values=list(
            analytics["threats"].values()
        ),




        timeline_labels=list(
            analytics["timeline"].keys()
        ),



        timeline_values=list(
            analytics["timeline"].values()
        )

    )