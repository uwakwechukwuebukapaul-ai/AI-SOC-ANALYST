from evidence_engine.email_analyzer import analyze_email



result = analyze_email(

"URGENT: Verify your account",

"security@micr0soft-login.xyz",

"Click here to verify your password https://micr0soft-login.xyz"

)


print(result)