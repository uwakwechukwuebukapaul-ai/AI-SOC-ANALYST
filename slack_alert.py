def send_slack_alert(report):

    print("===== SLACK ALERT =====")

    print("🚨 SECURITY ALERT")

    print(f"Risk Level: {report['risk']}")
    print(f"Risk Score: {report['score']}")

    print("\nIndicators:")

    for reason in report["reasons"]:
        print("-", reason)

    print("======================")