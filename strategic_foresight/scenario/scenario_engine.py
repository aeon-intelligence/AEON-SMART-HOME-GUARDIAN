def simulate(scenario, risk):

    return {
        "scenario": scenario,
        "risk": risk["risk_level"],
        "preparedness":
            "ACTION_REQUIRED"
            if risk["risk_level"] == "HIGH"
            else "MONITOR"
    }
