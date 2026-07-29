import requests
import os
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")


def check_ioc(ioc):
    """
    Check an IOC (currently supports domains)
    """

    if not VT_API_KEY:
        return {
            "error": "VirusTotal API key missing"
        }

    url = f"https://www.virustotal.com/api/v3/domains/{ioc}"

    headers = {
        "x-apikey": VT_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            data = response.json()

            stats = data["data"]["attributes"]["last_analysis_stats"]

            return {
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0),
                "harmless": stats.get("harmless", 0)
            }

        elif response.status_code == 404:
            return {
                "error": "IOC not found"
            }

        else:
            return {
                "error": f"VirusTotal returned {response.status_code}"
            }

    except Exception as e:
        return {
            "error": str(e)
        }


def check_domain(domain):
    """
    Backwards compatibility
    """
    return check_ioc(domain)