import re


def extract_iocs(text):

    iocs = {
        "emails": [],
        "domains": [],
        "ips": [],
        "urls": []
    }


    # Emails
    iocs["emails"] = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )


    # URLs
    iocs["urls"] = re.findall(
        r'https?://[^\s]+',
        text
    )


    # IP addresses
    iocs["ips"] = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )


    # Domains
    for email in iocs["emails"]:
        domain = email.split("@")[1]
        iocs["domains"].append(domain)


    return iocs



def analyze_email(sender, subject, body):

    text = sender + " " + subject + " " + body

    score = 0
    reasons = []


    keywords = [
        "urgent",
        "verify",
        "password",
        "login",
        "account",
        "suspended"
    ]


    for word in keywords:
        if word in text.lower():
            score += 2
            reasons.append(
                f"Suspicious keyword: {word}"
            )


    if "micr0soft" in text.lower():
        score += 5
        reasons.append(
            "Possible brand impersonation"
        )


    if score >= 8:
        risk = "HIGH"

    elif score >= 4:
        risk = "MEDIUM"

    else:
        risk = "LOW"


    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "iocs": extract_iocs(text)
    }