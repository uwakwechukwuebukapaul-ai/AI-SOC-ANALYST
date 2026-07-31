from evidence_engine.email_analyzer import email_analyzer


result = email_analyzer.analyze(

    subject="URGENT: Verify your account",

    sender="security@micr0soft-login.xyz",

    body="""
    Your account has been suspended.
    Click here immediately:
    https://micr0soft-login.xyz/verify
    """

)


print("=" * 50)

print("SENTINEL DNA EMAIL ANALYSIS")

print("=" * 50)


for key, value in result.items():

    print(
        f"\n{key.upper()}:"
    )

    print(value)