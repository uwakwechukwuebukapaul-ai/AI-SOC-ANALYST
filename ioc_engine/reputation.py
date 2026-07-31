"""
Sentinel DNA
IOC Reputation Engine

Version:
Enhanced Offline Threat Scoring Engine

Future Integrations:
- VirusTotal
- AbuseIPDB
- AlienVault OTX
- URLhaus
- OpenPhish
- GreyNoise
- Shodan
"""


from datetime import datetime



def check_reputation(ioc):

    value = ioc["value"].lower()


    reputation = {

        "checked": datetime.now().isoformat(),

        "ioc": value,

        "status": "UNKNOWN",

        "confidence": "LOW",

        "threat_score": 0,

        "risk_level": "LOW",

        "reasons": [],

        "source": "LOCAL"

    }



    indicators = {


        ".xyz": 25,

        ".ru": 20,

        ".top": 25,

        ".click": 25,

        ".zip": 15,


        "password": 20,

        "verify": 20,

        "login": 15,

        "admin": 10,

        "phishing": 30,


        "micr0soft": 35,

        "paypa1": 35,

        "secure-update": 25

    }



    for indicator, score in indicators.items():

        if indicator in value:

            reputation["threat_score"] += score

            reputation["reasons"].append(

                f"Matched indicator: {indicator}"

            )



    # Risk calculation

    score = reputation["threat_score"]



    if score >= 70:

        reputation["status"] = "MALICIOUS"

        reputation["confidence"] = "HIGH"

        reputation["risk_level"] = "CRITICAL"



    elif score >= 40:

        reputation["status"] = "SUSPICIOUS"

        reputation["confidence"] = "MEDIUM"

        reputation["risk_level"] = "HIGH"



    elif score > 0:

        reputation["status"] = "SUSPICIOUS"

        reputation["confidence"] = "LOW"

        reputation["risk_level"] = "MEDIUM"



    else:

        reputation["status"] = "CLEAN"

        reputation["confidence"] = "HIGH"

        reputation["risk_level"] = "LOW"



    return reputation




if __name__ == "__main__":


    sample = [


        {
            "type": "DOMAIN",
            "value": "micr0soft-login.xyz"
        },


        {
            "type": "URL",
            "value": "https://google.com"
        },


        {
            "type": "EMAIL",
            "value": "admin@evil.xyz"
        }

    ]


    print("🧬 IOC REPUTATION ENGINE TEST")

    print("=" * 45)



    for ioc in sample:

        print()

        print(check_reputation(ioc))