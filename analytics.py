from database import get_incidents



def get_analytics():


    incidents = get_incidents()



    total = len(incidents)


    high = 0

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



        if status == "OPEN":

            open_cases += 1


        elif status == "INVESTIGATING":

            investigating += 1


        elif status == "RESOLVED":

            resolved += 1



        if threat not in attack_types:

            attack_types[threat] = 0


        attack_types[threat] += 1



        risk_scores.append(score)



    average_risk = 0


    if risk_scores:

        average_risk = sum(risk_scores) / len(risk_scores)



    maximum_risk = 0


    if risk_scores:

        maximum_risk = max(risk_scores)



    return {


        "total": total,


        "high": high,


        "open": open_cases,


        "investigating": investigating,


        "resolved": resolved,


        "attack_types": attack_types,


        "average_risk": round(average_risk, 2),


        "maximum_risk": maximum_risk


    }



if __name__ == "__main__":


    data = get_analytics()


    print("📊 SOC ANALYTICS")

    print("=" * 40)


    for key, value in data.items():

        print(key, ":", value)