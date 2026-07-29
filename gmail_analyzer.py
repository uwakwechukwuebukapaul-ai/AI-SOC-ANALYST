import re


def analyze_email(subject, sender, body):

    score = 0
    reasons = []

    email_text = (subject + " " + sender + " " + body).lower()

    # Phishing keywords
    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "login",
        "bank",
        "account suspended",
        "click here",
        "confirm",
        "security alert"
    ]

    # Check suspicious words
    for word in suspicious_words:
        if word in email_text:
            score += 1
            reasons.append(f"Suspicious keyword detected: {word}")

    # URL detection
    urls = re.findall(r'https?://\S+', body)

    for url in urls:
        score += 2
        reasons.append(f"Suspicious URL detected: {url}")

    # Sender analysis
    suspicious_domains = [
        "xyz",
        "top",
        "click",
        "login",
        "verify"
    ]

    for domain in suspicious_domains:
        if domain in sender.lower():
            score += 2
            reasons.append(
                f"Suspicious sender domain detected: {domain}"
            )

    # Risk calculation
    if score >= 5:
        risk = "HIGH"

    elif score >= 3:
        risk = "MEDIUM"

    else:
        risk = "LOW"


    return {
        "risk": risk,
        "score": score,
        "reasons": reasons
    }