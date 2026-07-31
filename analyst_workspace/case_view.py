"""
Sentinel DNA
Case Viewer
"""


from database.repository import get_cases



def view_cases():

    cases = get_cases()


    for case in cases:

        print("\n🧬 CASE DETAILS")

        print("="*30)

        for key,value in case.items():

            print(
                f"{key}: {value}"
            )



if __name__ == "__main__":

    view_cases()