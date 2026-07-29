import requests
import os
import re

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("VT_API_KEY")


BASE_URL = "https://www.virustotal.com/api/v3"



def extract_domain(text):

    urls = re.findall(
        r'https?://([^/\s]+)',
        text
    )

    if urls:

        return urls[0]

    return None





def check_domain(domain):


    if not API_KEY:

        return {

            "error": "VirusTotal API key missing"

        }



    headers = {

        "x-apikey": API_KEY

    }


    url = f"{BASE_URL}/domains/{domain}"


    response = requests.get(

        url,

        headers=headers

    )



    if response.status_code != 200:

        return {

            "domain": domain,

            "status": "NOT FOUND"

        }



    data = response.json()



    stats = data["data"]["attributes"]["last_analysis_stats"]



    malicious = stats.get("malicious", 0)

    suspicious = stats.get("suspicious", 0)

    harmless = stats.get("harmless", 0)



    # Improved SOC verdict

    if malicious > 0:

        verdict = "MALICIOUS"



    elif suspicious > 0:

        verdict = "SUSPICIOUS"



    else:

        verdict = "CLEAN"




    return {


        "domain": domain,

        "malicious": malicious,

        "suspicious": suspicious,

        "harmless": harmless,

        "status": verdict

    }





def analyze_indicator(text):


    domain = extract_domain(text)



    if not domain:

        return {

            "status": "No domain found"

        }



    return check_domain(domain)






if __name__ == "__main__":


    test = (

        "https://micr0soft-login.xyz/verify"

    )


    result = analyze_indicator(test)



    print("🌐 THREAT INTELLIGENCE RESULT")

    print("=" * 40)



    for key, value in result.items():

        print(

            key,

            ":",

            value

        )