def recommend_recovery(status):

    if status == "DEGRADED":

        return {
            "recommendation":
                "AUTO_OPTIMIZATION_REQUIRED"
        }

    return {
        "recommendation":
            "CONTINUE_MONITORING"
    }
