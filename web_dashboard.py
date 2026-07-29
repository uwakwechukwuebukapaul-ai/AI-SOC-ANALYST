from flask import Flask, render_template

from soc_pipeline import run_soc_pipeline


app = Flask(__name__)


@app.route("/")
def home():

    alerts = run_soc_pipeline()


    return render_template(
        "index.html",
        alerts=alerts
    )



if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )