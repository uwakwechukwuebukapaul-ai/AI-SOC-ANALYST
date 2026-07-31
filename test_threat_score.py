from core.risk_engine.threat_scorer import threat_scorer


email = {

    "risk": "HIGH",

    "evidence":[

        "Suspicious URL",

        "Fake domain"

    ]

}


ioc = {

    "indicators":{

        "url":[
            "https://fake-login.xyz"
        ],

        "md5":[
            "44d88612fea8a8f36de82e1278abb02f"
        ]

    }

}



result = threat_scorer.analyze(

    email,

    ioc

)


print("="*50)

print("SENTINEL DNA THREAT SCORE")

print("="*50)


for key,value in result.items():

    print(
        key,
        ":",
        value
    )