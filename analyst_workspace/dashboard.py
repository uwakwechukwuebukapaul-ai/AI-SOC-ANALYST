"""
Sentinel DNA
Analyst Workspace Dashboard

SOC Analyst case overview
"""


from database.repository import get_cases



def show_dashboard():

    cases = get_cases()


    print("🧬 SENTINEL DNA ANALYST WORKSPACE")

    print("=" * 45)


    print(
        f"Total Cases: {len(cases)}"
    )


    for case in cases:

        print("\n--------------------")

        print(
            "Case ID:",
            case["case_id"]
        )

        print(
            "Title:",
            case["title"]
        )

        print(
            "Severity:",
            case["severity"]
        )

        print(
            "Status:",
            case["status"]
        )



if __name__ == "__main__":

    show_dashboard()