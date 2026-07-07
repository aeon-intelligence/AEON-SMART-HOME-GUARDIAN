def generate_heatmap(signals):

    return {
        "critical_area": [
            signal["area"]
            for signal in signals
            if signal["risk"] >= 80
        ],
        "risk_level":
            "HIGH"
            if any(
                s["risk"] >= 80
                for s in signals
            )
            else "NORMAL"
    }
