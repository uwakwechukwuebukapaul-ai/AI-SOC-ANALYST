"""
Sentinel DNA
Dashboard Analytics Engine

Provides:
- Case statistics
- Severity analytics
- Threat analytics
- Timeline analytics
- AI risk overview
"""


from database.connection import database





# =====================================
# TOTAL CASE STATISTICS
# =====================================

def get_case_statistics():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT COUNT(*) 
            FROM cases
            """
        )

        total_cases = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)
            FROM cases
            WHERE severity='HIGH'
            """
        )

        high_cases = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)
            FROM cases
            WHERE status='OPEN'
            """
        )

        open_cases = cursor.fetchone()[0]



        cursor.execute(
            """
            SELECT COUNT(*)
            FROM cases
            WHERE status='CLOSED'
            """
        )

        closed_cases = cursor.fetchone()[0]



    return {

        "total_cases": total_cases,

        "high_cases": high_cases,

        "open_cases": open_cases,

        "closed_cases": closed_cases

    }






# =====================================
# SEVERITY DISTRIBUTION
# =====================================

def get_severity_distribution():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT severity, COUNT(*)

            FROM cases

            GROUP BY severity

            """
        )


        results = cursor.fetchall()



    return {

        row[0]: row[1]

        for row in results

    }






# =====================================
# STATUS DISTRIBUTION
# =====================================

def get_status_distribution():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT status, COUNT(*)

            FROM cases

            GROUP BY status

            """
        )


        results = cursor.fetchall()



    return {

        row[0]: row[1]

        for row in results

    }






# =====================================
# THREAT TYPE ANALYTICS
# =====================================

def get_threat_distribution():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT title, COUNT(*)

            FROM cases

            GROUP BY title

            ORDER BY COUNT(*) DESC

            LIMIT 10

            """
        )


        results = cursor.fetchall()



    return {

        row[0]: row[1]

        for row in results

    }






# =====================================
# INCIDENT TIMELINE ANALYTICS
# =====================================

def get_incident_timeline():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT substr(created,1,10),
                   COUNT(*)

            FROM cases

            GROUP BY substr(created,1,10)

            ORDER BY created

            """
        )


        results = cursor.fetchall()



    return {

        row[0]: row[1]

        for row in results

    }






# =====================================
# AI RISK OVERVIEW
# =====================================

def get_ai_risk_summary():

    stats = get_case_statistics()


    risk_level = "LOW"


    if stats["high_cases"] > 0:

        risk_level = "HIGH"



    return {

        "risk_level": risk_level,

        "critical_cases": stats["high_cases"],

        "total_incidents": stats["total_cases"]

    }






# =====================================
# COMPLETE DASHBOARD DATA
# =====================================

def get_dashboard_analytics():


    return {


        "statistics":

            get_case_statistics(),


        "severity":

            get_severity_distribution(),


        "status":

            get_status_distribution(),


        "threats":

            get_threat_distribution(),


        "timeline":

            get_incident_timeline(),


        "risk":

            get_ai_risk_summary()

    }