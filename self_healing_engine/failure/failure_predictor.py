def predict_failure(health):

    return {
        "failure_probability":
            100 - health["health_score"],
        "prediction":
            "MONITOR"
            if health["health_score"] > 80
            else "ACTION_REQUIRED"
    }
