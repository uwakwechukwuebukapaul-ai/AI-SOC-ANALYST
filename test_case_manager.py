from cases.case_manager import create_investigation


case = create_investigation(

    title="Malicious Email Detection",

    severity="HIGH",

    description=
    "Credential phishing attempt detected",

    evidence=[

        {
            "type":"domain",
            "value":"fake-login.xyz"
        }

    ]

)


print(case)