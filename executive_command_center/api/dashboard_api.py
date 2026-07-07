from executive_command_center.dashboard.dashboard import generate_dashboard


def get_dashboard():

    signal = {
        "priority": "CRITICAL",
        "risk_score": 91,
        "business_impact": {
            "operation": "INVENTORY"
        }
    }

    return generate_dashboard(signal)


if __name__ == "__main__":
    print(get_dashboard())
