from cases.case_manager import case_manager

from cases.evidence import add_evidence

from cases.timeline import add_event



case = case_manager.create_case(

    "Phishing Attack Investigation",

    "HIGH",

    "Suspicious email campaign detected"

)



add_evidence(

    case,

    "URL",

    "https://fake-login.xyz"

)



add_event(

    case,

    "Email analyzed by evidence engine"

)



print("="*50)

print("SENTINEL DNA CASE")

print("="*50)


print(case)