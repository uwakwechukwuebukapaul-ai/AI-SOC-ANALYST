from cases.timeline import (
    add_timeline_event,
    get_timeline
)

from database.repository import create_case



TEST_CASE = {
    "case_id": "INC-20260731-TEST01",
    "title": "Timeline Test Case",
    "severity": "HIGH",
    "description": "Testing timeline engine"
}



# Create parent case first

try:

    create_case(TEST_CASE)

except Exception:

    pass



# Add timeline event

event = add_timeline_event(

    TEST_CASE["case_id"],

    "ALERT",

    "Suspicious phishing email detected",

    "AI ENGINE"

)



print("=" * 50)

print("SENTINEL DNA TIMELINE TEST")

print("=" * 50)


print(event)



timeline = get_timeline(

    TEST_CASE["case_id"]

)


print("\nTIMELINE RECORDS")

print("=" * 50)


for item in timeline:

    print(item)