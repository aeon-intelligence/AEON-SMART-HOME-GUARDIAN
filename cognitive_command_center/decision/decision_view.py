def create_decision_view(kpi, risk):

    return {
        "kpi": kpi,
        "risk": risk,
        "recommended_action":
            "EXECUTIVE_REVIEW"
            if risk["level"] == "HIGH"
            else "CONTINUE"
    }
