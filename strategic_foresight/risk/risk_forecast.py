def forecast(signal):

    risk_level = (
        "HIGH"
        if signal["impact"] > 80
        else "MEDIUM"
    )

    return {
        "risk_level": risk_level,
        "signal": signal["source"]
    }
