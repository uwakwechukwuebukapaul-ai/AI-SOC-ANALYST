import sqlite3
import json
from datetime import datetime


conn = sqlite3.connect("soc_incidents.db")

cursor = conn.cursor()



timeline = json.dumps([

    {
        "time": "09:55:45",
        "event": "Phishing email detected"
    },

    {
        "time": "09:55:46",
        "event": "Suspicious domain extracted"
    },

    {
        "time": "09:55:47",
        "event": "VirusTotal reputation checked"
    },

    {
        "time": "09:55:48",
        "event": "Risk score calculated"
    },

    {
        "time": "09:55:49",
        "event": "Containment initiated"
    }

])



evidence = json.dumps({

    "Sender":
    "security@micr0soft-login.xyz",

    "Domain":
    "micr0soft-login.xyz",

    "Indicators":
    "Urgent keyword, suspicious URL, credential request",

    "Threat Intelligence":
    "VirusTotal status: SUSPICIOUS"

})



cursor.execute(

"""

UPDATE incidents

SET timeline=?,
evidence=?

WHERE id=5

""",

(

timeline,

evidence

)

)



conn.commit()

conn.close()


print("✅ Case evidence and timeline updated")