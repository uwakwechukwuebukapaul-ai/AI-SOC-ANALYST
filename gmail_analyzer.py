import re


def analyze_email(subject, sender, body):
    score = 0
    reasons = []

    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "login",
        "bank",
        "account suspended",
        "click here",
    ]

    for word in suspicious_words:
        if word.lower() in subject.lower() or word.lower() in body.lower():
            score += 1
            reasons.append(f"Suspicious keyword: {word}")

    trusted_domains = [
        "microsoft.com",
        "google.com",
        "github.com",
    ]

    if "@" in sender:
        domain = sender.split("@")[1].lower()

        if domain not in trusted_domains:
            score += 2
            reasons.append(f"Suspicious sender domain: {domain}")
    else:
        score += 2
        reasons.append("Invalid sender email")

    urls = re.findall(r"https?://[^\s]+", body)

    for url in urls:
        score += 2
        reasons.append(f"URL found in email body: {url}")

        suspicious_url_signs = [
            ".xyz",
            ".ru",
            "login",
            "verify",
            "security",
            "password",
        ]

        for sign in suspicious_url_signs:
            if sign in url.lower():
                score += 2
                reasons.append(f"Suspicious URL detected: {url}")
                break

    if score >= 7:
        risk = "HIGH"
    elif score >= 4:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "urls": urls,
    }