def analyze_risk(signal):

    return {
        "risk_score":
            signal["value"],
        "level":
            "HIGH"
            if signal["value"] > 80
            else "NORMAL"
    }
