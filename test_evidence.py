from cases.evidence import add_evidence


case = {

    "case_id":
        "INC-20260731-TEST",

    "evidence":[]

}



result = add_evidence(

    case,

    "URL",

    "https://fake-login.xyz"

)



print("🧬 SENTINEL DNA EVIDENCE")

print("="*40)

print(result)