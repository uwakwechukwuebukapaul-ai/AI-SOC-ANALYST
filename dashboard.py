"""
Sentinel DNA
Dashboard Analytics Engine

SOC Metrics:
- Cases
- Critical Threats
- Evidence Collection
- IOC Intelligence
- Phishing Alerts
"""


from flask import render_template


from database.repository import (
    get_cases,
    get_evidence,
    get_iocs
)





def dashboard():


    cases = get_cases()

    evidence = get_evidence()

    iocs = get_iocs()



    # ==============================
    # FIX CASE ID FOR DASHBOARD LINKS
    # ==============================

    for case in cases:

        if not case.get("case_id"):

            case["case_id"] = (
                case.get("id")
                or "UNKNOWN"
            )





    # ==============================
    # CASE METRICS
    # ==============================


    total_cases = len(cases)



    critical_cases = len(
        [
            c for c in cases
            if c.get("severity") == "CRITICAL"
        ]
    )



    high_cases = len(
        [
            c for c in cases
            if c.get("severity") == "HIGH"
        ]
    )



    open_cases = len(
        [
            c for c in cases
            if c.get("status") == "OPEN"
        ]
    )



    closed_cases = len(
        [
            c for c in cases
            if c.get("status") == "CLOSED"
        ]
    )





    phishing_alerts = len(
        [
            c for c in cases
            if "Phishing" in c.get(
                "title",
                ""
            )
        ]
    )





    stats = {


        "total_cases":
            total_cases,


        "critical_cases":
            critical_cases,


        "high_cases":
            high_cases,


        "open_cases":
            open_cases,


        "closed_cases":
            closed_cases,


        "evidence_count":
            len(evidence),


        "ioc_count":
            len(iocs),


        "phishing_alerts":
            phishing_alerts,


        "cases":
            cases

    }





    # ==============================
    # SEVERITY DATA
    # ==============================


    severity = {}



    for case in cases:


        level = case.get(
            "severity",
            "UNKNOWN"
        )


        severity[level] = severity.get(
            level,
            0
        ) + 1







    # ==============================
    # THREAT CATEGORY DATA
    # ==============================


    threats = {}



    for case in cases:


        title = case.get(
            "title",
            "Unknown"
        )


        threats[title] = threats.get(
            title,
            0
        ) + 1







    # ==============================
    # TIMELINE DATA
    # ==============================


    timeline = {}



    for case in cases:


        date = case.get(
            "created",
            ""
        )[:10]


        timeline[date] = timeline.get(
            date,
            0
        ) + 1







    analytics = {


        "risk": {


            "risk_level":

                "CRITICAL"

                if critical_cases > 0

                else "NORMAL",



            "critical_cases":

                critical_cases,



            "total_incidents":

                total_cases

        }

    }





    return render_template(


        "dashboard.html",


        stats=stats,


        analytics=analytics,


        severity_labels=list(
            severity.keys()
        ),


        severity_values=list(
            severity.values()
        ),


        threat_labels=list(
            threats.keys()
        ),


        threat_values=list(
            threats.values()
        ),


        timeline_labels=list(
            timeline.keys()
        ),


        timeline_values=list(
            timeline.values()
        )

    )