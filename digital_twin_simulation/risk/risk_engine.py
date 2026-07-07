def calculate_risk(simulation):

    if simulation["status"] == "RISK":
        return {
            "risk_score": 85,
            "recommendation": "Prepare mitigation plan"
        }

    return {
        "risk_score": 20,
        "recommendation": "Continue monitoring"
    }
