"""
Sentinel DNA
Dashboard Analytics Route

Provides:
- Case statistics
- Severity analytics
- Threat categories
- Timeline analytics
- SOC metrics
"""


from pathlib import Path
import sys


from flask import render_template



PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


if str(PROJECT_ROOT) not in sys.path:

    sys.path.append(str(PROJECT_ROOT))



from database.repository import get_cases



try:

    from database.repository import get_evidence

except ImportError:

    get_evidence = None



try:

    from database.repository import get_iocs

except ImportError:

    get_iocs = None







def dashboard():


    cases = get_cases()



    # =================================
    # BASIC CASE STATISTICS
    # =================================


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



    medium_cases = len(

        [

            c for c in cases

            if c.get("severity") == "MEDIUM"

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






    # =================================
    # SECURITY METRICS
    # =================================


    evidence_count = 0


    ioc_count = 0



    if get_evidence:

        try:

            evidence_count = len(get_evidence())

        except:

            evidence_count = 0



    if get_iocs:

        try:

            ioc_count = len(get_iocs())

        except:

            ioc_count = 0






    phishing_cases = len(

        [

            c for c in cases

            if "phishing"

            in c.get("title","").lower()

        ]

    )







    stats = {


        "total_cases":

            total_cases,


        "critical_cases":

            critical_cases,


        "high_cases":

            high_cases,


        "medium_cases":

            medium_cases,


        "open_cases":

            open_cases,


        "closed_cases":

            closed_cases,


        "evidence_count":

            evidence_count,


        "ioc_count":

            ioc_count,


        "phishing_cases":

            phishing_cases,


        "cases":

            cases

    }








    # =================================
    # SEVERITY ANALYTICS
    # =================================


    severity = {}



    for case in cases:


        level = case.get(

            "severity",

            "UNKNOWN"

        )


        severity[level] = (

            severity.get(level,0)

            + 1

        )









    # =================================
    # THREAT CATEGORY ANALYTICS
    # =================================


    threats = {}



    for case in cases:


        title = case.get(

            "title",

            "UNKNOWN"

        )



        threats[title] = (

            threats.get(title,0)

            + 1

        )









    # =================================
    # INCIDENT TIMELINE
    # =================================


    timeline = {}



    for case in cases:


        date = case.get(

            "created",

            ""

        )[:10]



        timeline[date] = (

            timeline.get(date,0)

            + 1

        )










    # =================================
    # AI RISK OVERVIEW
    # =================================


    if critical_cases > 0:

        risk_level = "CRITICAL"


    elif high_cases > 0:

        risk_level = "HIGH"


    elif medium_cases > 0:

        risk_level = "MEDIUM"


    else:

        risk_level = "LOW"







    analytics = {


        "risk": {


            "risk_level":

                risk_level,


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