"""
Sentinel DNA
Dashboard Analytics Route
"""

from pathlib import Path
import sys

from flask import render_template


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


from database.repository import get_cases



def dashboard():

    cases = get_cases()


    stats = {

        "total_cases": len(cases),

        "high_cases": len(
            [
                c for c in cases
                if c.get("severity") == "HIGH"
            ]
        ),

        "open_cases": len(
            [
                c for c in cases
                if c.get("status") == "OPEN"
            ]
        ),


        "closed_cases": len(
            [
                c for c in cases
                if c.get("status") == "CLOSED"
            ]
        ),


        "cases": cases

    }



    # ================================
    # Severity Analytics
    # ================================


    severity = {}


    for case in cases:

        level = case.get("severity","UNKNOWN")

        severity[level] = severity.get(level,0)+1






    # ================================
    # Threat Analytics
    # ================================


    threats = {}


    for case in cases:

        title = case.get("title","Unknown")

        threats[title] = threats.get(title,0)+1








    # ================================
    # Timeline Analytics
    # ================================


    timeline = {}


    for case in cases:

        date = case.get("created","")[:10]

        timeline[date] = timeline.get(date,0)+1






    analytics = {


        "risk": {

            "risk_level":"HIGH",

            "critical_cases":stats["high_cases"],

            "total_incidents":stats["total_cases"]

        }


    }





    return render_template(

        "dashboard.html",

        stats=stats,

        analytics=analytics,


        severity_labels=list(severity.keys()),

        severity_values=list(severity.values()),


        threat_labels=list(threats.keys()),

        threat_values=list(threats.values()),


        timeline_labels=list(timeline.keys()),

        timeline_values=list(timeline.values())

    )