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
        "click here"
    ]

    for word in suspicious_words:
        if word.lower() in subject.lower() or word.lower() in body.lower():
            score += 1
            reasons.append(f"Suspicious keyword: {word}")

    trusted_domains = [
        "microsoft.com",
        "google.com",
        "github.com"
    ]

    if "@" in sender:
        domain = sender.split("@")[1]

        if domain not in trusted_domains:
            score += 2
            reasons.append(f"Suspicious sender domain: {domain}")
    else:
        score += 2
        reasons.append("Invalid sender email")

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