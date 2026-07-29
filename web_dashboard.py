from flask import Flask, render_template, request

from soc_analytics import (
    total_incidents,
    risk_summary,
    latest_incident
)

from threat_intel import check_ioc


app = Flask(__name__)


# =========================
# MAIN DASHBOARD
# =========================

@app.route("/")
def home():

    total = total_incidents()

    summary = risk_summary()

    latest = latest_incident()


    stats = {

        "total": total,

        "risks": {

            "HIGH": summary.get("HIGH", 0),

            "MEDIUM": summary.get("MEDIUM", 0),

            "LOW": summary.get("LOW", 0)

        }

    }


    # Threat Intelligence

    if latest:

        reputation = check_ioc(latest["sender"])

    else:

        reputation = {

            "error": "No incident available"

        }



    # MITRE ATT&CK Mapping

    mitre = {

        "HIGH":
        "T1566.001 - Spearphishing Attachment",

        "MEDIUM":
        "T1566 - Phishing",

        "LOW":
        "Informational"

    }



    if latest:

        attack = mitre.get(
            latest["risk"],
            "Unknown"
        )

    else:

        attack = "Unknown"



    return render_template(

        "index.html",

        stats=stats,

        latest=latest,

        reputation=reputation,

        attack=attack

    )



# =========================
# IOC LOOKUP PAGE
# =========================

@app.route("/ioc", methods=["GET", "POST"])
def ioc_lookup():

    result = None


    if request.method == "POST":

        ioc = request.form.get("ioc")


        if ioc:

            result = check_ioc(ioc)



    return render_template(

        "ioc.html",

        result=result

    )



# =========================
# START SERVER
# =========================

if __name__ == "__main__":

    app.run(debug=True)