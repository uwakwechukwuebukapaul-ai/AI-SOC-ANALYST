from gmail_analyzer import analyze_email
from slack_alert import send_slack_alert
from incident_logger import save_incident


print("=" * 50)
print("🛡️ AI SOC ANALYST")
print("=" * 50)


# Collect email information
subject = input("\nEnter Email Subject: ")

sender = input("Enter Sender Email: ")

print("\nPaste Email Body (type END when finished):")

body_lines = []

while True:
    line = input()

    if line == "END":
        break

    body_lines.append(line)

body = "\n".join(body_lines)


# Analyze email
result = analyze_email(subject, sender, body)


# Display incident report
print("\n===== INCIDENT REPORT =====")

print(f"Risk Level : {result['risk']}")
print(f"Risk Score : {result['score']}")


print("\nIndicators Found:")

if result["reasons"]:
    for reason in result["reasons"]:
        print(f"• {reason}")
else:
    print("• No suspicious indicators found")


# Send Slack alert if high risk
if result["risk"] == "HIGH":
    send_slack_alert(result)


# Save incident to CSV
save_incident(sender, subject, result)


print("\nInvestigation Complete ✅")