from datetime import datetime



def automated_response(alert):


    actions = []


    threat = alert.get(
        "type",
        ""
    ).lower()



    if "phishing" in threat:


        actions = [

            "Block malicious sender",

            "Remove phishing emails",

            "Reset affected credentials",

            "Enable MFA",

            "Investigate suspicious domain",

            "Escalate incident to SOC analyst"

        ]


    else:


        actions = [

            "Investigate alert",

            "Collect evidence",

            "Escalate to SOC analyst"

        ]




    return {


        "incident":

        alert.get("type"),


        "time":

        str(datetime.now()),


        "severity":

        alert.get("severity"),


        "automated_actions":

        actions,


        "status":

        "CONTAINMENT INITIATED"

    }





# Compatibility with older files

def generate_response(alert):

    return automated_response(alert)