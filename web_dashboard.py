"""
Sentinel DNA
Web Dashboard Server

Main Flask Application
"""


from flask import Flask, render_template


from dashboard import dashboard



app = Flask(__name__)





# =====================================
# DASHBOARD ROUTE
# =====================================


@app.route("/")
def home():

    return dashboard()





# =====================================
# CASE VIEW PLACEHOLDER
# =====================================


@app.route("/case/<case_id>")
def case_view(case_id):

    return f"""
    <h1>🧬 Sentinel DNA Case Investigation</h1>

    <h3>Case ID:</h3>

    <p>{case_id}</p>

    <hr>

    Investigation module coming next...

    """





if __name__ == "__main__":


    print(
        "🧬 Sentinel DNA SOC Dashboard Running"
    )


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )