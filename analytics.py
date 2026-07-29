from database import get_incidents



def get_analytics():

    incidents = get_incidents()


    total = len(incidents)

    high = 0
    medium = 0
    low = 0

    open_cases = 0
    investigating = 0
    resolved = 0


    attack_types = {}

    risk_scores = []



    for incident in incidents:


        severity = incident[3]

        status = incident[6]

        threat = incident[2]

        score = incident[4]



        if severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1



        if status == "OPEN":
            open_cases += 1

        elif status == "INVESTIGATING":
            investigating += 1

        elif status == "RESOLVED":
            resolved += 1



        attack_types[threat] = attack_types.get(threat, 0) + 1


        risk_scores.append(score)



    average_risk = 0

    if risk_scores:
        average_risk = sum(risk_scores) / len(risk_scores)



    return {


        "total": total,

        "high": high,

        "medium": medium,

        "low": low,


        "open": open_cases,

        "investigating": investigating,

        "resolved": resolved,


        "attack_types": attack_types,


        "average_risk": round(average_risk,2),


        "maximum_risk": max(risk_scores) if risk_scores else 0

    }