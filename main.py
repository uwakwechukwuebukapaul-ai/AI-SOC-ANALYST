from gmail_analyzer import analyze_email

subject = "URGENT: Verify your account"
sender = "security@micr0soft-login.xyz"
body = """
Your account has been suspended.
Click here immediately to verify your password.
"""

result = analyze_email(subject, sender, body)

print("===== AI SOC ANALYST REPORT =====")
print(f"Risk Level: {result['risk']}")
print(f"Risk Score: {result['score']}")
print("Reasons:")

for reason in result["reasons"]:
    print("-", reason)