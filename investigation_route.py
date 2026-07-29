from flask import jsonify

from ai_investigator import investigate_alert

from database import get_incidents



def get_investigation_report(incident_id):

    incidents = get_incidents()


    selected_incident = None


    for incident in incidents:

        if incident[0] == incident_id:

            selected_incident = incident

            break



    if not selected_incident:

        return {

            "error": "Incident not found"

        }



    alert = {

        "type": selected_incident[2],

        "severity": selected_incident[3],

        "score": selected_incident[4],

        "mitre": selected_incident[5]

    }



    report = investigate_alert(alert)


    return report





if __name__ == "__main__":


    print("🤖 AI SOC INVESTIGATION ROUTE")

    print("=" * 40)


    incidents = get_incidents()


    if not incidents:

        print("No incidents available")



    else:


        incident_id = incidents[0][0]


        report = get_investigation_report(incident_id)


        print("\nInvestigation Report")

        print("--------------------")


        for key, value in report.items():

            print("\n" + key.upper())

            print(value)