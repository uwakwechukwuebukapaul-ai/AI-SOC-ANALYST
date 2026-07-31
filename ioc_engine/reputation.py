"""
Sentinel DNA
IOC Reputation Engine

Future Integrations:
- VirusTotal
- AbuseIPDB
- AlienVault OTX
- URLhaus
- OpenPhish
- GreyNoise
- Shodan

Current Version:
Offline reputation engine.
"""

from datetime import datetime


def check_reputation(ioc):

    value = ioc["value"].lower()

    reputation = {

        "checked": datetime.now().isoformat(),

        "ioc": value,

        "status": "UNKNOWN",

        "confidence": "LOW",

        "source": "LOCAL"

    }

    suspicious = [

        ".xyz",
        ".ru",
        ".top",
        ".click",
        ".zip",

        "password",

        "verify",

        "login",

        "admin",

        "phishing"

    ]

    for indicator in suspicious:

        if indicator in value:

            reputation["status"] = "SUSPICIOUS"

            reputation["confidence"] = "HIGH"

            break

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

    print("🧬 IOC REPUTATION TEST")

    print("=" * 40)

    for ioc in sample:

        print()

        print(check_reputation(ioc))