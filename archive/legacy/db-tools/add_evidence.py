import sqlite3
import json


conn = sqlite3.connect("soc_incidents.db")

cursor = conn.cursor()



timeline = [

    {
        "time": "09:55:45",
        "event": "Phishing alert detected by SOC engine"
    },

    {
        "time": "09:55:46",
        "event": "Suspicious domain extracted: micr0soft-login.xyz"
    },

    {
        "time": "09:55:47",
        "event": "VirusTotal reputation lookup completed"
    },

    {
        "time": "09:55:48",
        "event": "Risk score calculated: 90 (HIGH)"
    },

    {
        "time": "09:55:49",
        "event": "Automated containment initiated"
    }

]




evidence = {

    "Sender":
    "security@micr0soft-login.xyz",

    "Domain":
    "micr0soft-login.xyz",

    "Threat Intelligence":
    "VirusTotal Status: SUSPICIOUS",

    "Indicators":
    "Suspicious URL, credential harvesting attempt, phishing keywords"

}




cursor.execute(

"""

UPDATE incidents

SET timeline=?,
evidence=?

WHERE id=5

""",

(

json.dumps(timeline),

json.dumps(evidence)

)

)



conn.commit()

conn.close()


print("✅ Evidence and timeline added to Incident #5")