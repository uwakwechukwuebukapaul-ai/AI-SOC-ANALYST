"""
Sentinel DNA
Web Dashboard Server

Main Flask Application
"""


from flask import Flask, render_template


from dashboard import dashboard

from investigation_route import (
    get_investigation_report
)



app = Flask(__name__)





# =====================================
# DASHBOARD ROUTE
# =====================================

@app.route("/")
def home():

    return dashboard()





# =====================================
# CASE INVESTIGATION VIEW
# =====================================

@app.route("/case/<case_id>")
def case_view(case_id):


    report = get_investigation_report(
        case_id
    )


    if not report:

        return """
        <h1>
        🧬 Sentinel DNA
        </h1>

        <h3>
        Case not found
        </h3>
        """



    return render_template(
        "investigation.html",
        report=report
    )







# =====================================
# START SERVER
# =====================================


if __name__ == "__main__":


    print(
        "🧬 Sentinel DNA SOC Dashboard Running"
    )


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )