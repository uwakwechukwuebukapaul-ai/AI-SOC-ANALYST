from database import get_incidents
from datetime import datetime



def get_live_monitor():

    incidents = get_incidents()


    if not incidents:

        return {

            "status": "NO ALERTS",

            "last_check": str(datetime.now()),

            "latest": None

        }



    latest = incidents[0]


    return {


        "status": "ACTIVE",


        "last_check": str(datetime.now()),


        "latest": {

            "id": latest[0],

            "time": latest[1],

            "threat": latest[2],

            "severity": latest[3],

            "score": latest[4],

            "status": latest[6]

        }

    }





if __name__ == "__main__":


    monitor = get_live_monitor()


    print("⚡ REAL-TIME SOC MONITOR")

    print("=" * 40)


    print(monitor)