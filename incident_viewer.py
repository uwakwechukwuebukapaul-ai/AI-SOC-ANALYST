import sqlite3
import json


DB_NAME = "soc_incidents.db"



def view_incidents():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM incidents ORDER BY id DESC"
    )


    incidents = cursor.fetchall()


    conn.close()



    print("🛡️ STORED SOC INCIDENTS")

    print("=" * 40)



    if not incidents:

        print("No incidents found")

        return



    for incident in incidents:


        print("\n--------------------")


        print("ID:", incident[0])

        print("Time:", incident[1])

        print("Threat:", incident[2])

        print("Severity:", incident[3])

        print("Risk Score:", incident[4])

        print("MITRE:", incident[5])

        print("Status:", incident[6])



        # New Response Information

        print("\n⚡ AUTOMATED RESPONSE")


        print(

            "Response Status:",

            incident[7]

        )


        print(

            "Response Time:",

            incident[9]

        )



        print("Actions:")



        try:

            actions = json.loads(

                incident[8]

            )


            for action in actions:

                print("-", action)



        except:

            print("No response actions")







if __name__ == "__main__":


    view_incidents()