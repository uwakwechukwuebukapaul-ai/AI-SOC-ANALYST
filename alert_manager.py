from soc_pipeline import run_soc_pipeline


def get_alerts():

    alerts = run_soc_pipeline()

    return alerts


if __name__ == "__main__":

    results = get_alerts()

    print("🚨 SOC ALERT MANAGER")
    print("=" * 40)

    for alert in results:
        print(alert)