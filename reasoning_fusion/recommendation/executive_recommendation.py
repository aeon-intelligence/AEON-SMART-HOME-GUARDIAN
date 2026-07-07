def generate_recommendation(impact):

    if impact["impact_level"] == "HIGH":

        return {
            "priority": "CRITICAL",
            "recommendation":
                "Execute mitigation workflow"
        }

    return {
        "priority": "NORMAL",
        "recommendation":
            "Continue monitoring"
    }
