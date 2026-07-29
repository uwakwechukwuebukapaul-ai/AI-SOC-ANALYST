from database import get_incidents


def get_dashboard_data():

    incidents = get_incidents()


    total = len(incidents)


    high = 0
    medium = 0
    low = 0
    open_cases = 0


    for incident in incidents:

        severity = incident[3]


        if severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1


        if incident[6] == "OPEN":
            open_cases += 1



    return {

        "total": total,

        "high": high,

        "medium": medium,

        "low": low,

        "open": open_cases,

        "incidents": incidents[:10]

    }