from cases.timeline import add_timeline_event, get_timeline


case = {

    "case_id":
        "INC-20260731-TEST"

}



add_timeline_event(

    case,

    "INVESTIGATION",

    "Analyst started investigation",

    "SOC ANALYST"

)



add_timeline_event(

    case,

    "CONTAINMENT",

    "Suspicious URL blocked"

)



print("🧬 TIMELINE TEST")

print("="*40)


for item in get_timeline(case):

    print(item)