from database import get_incidents


def display_incidents():

    incidents = get_incidents()

    print("\n🛡️ STORED SOC INCIDENTS")
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



if __name__ == "__main__":

    display_incidents()