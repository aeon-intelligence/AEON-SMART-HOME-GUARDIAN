def detect_incident(metrics):

    if metrics["latency_ms"] > 500:

        return {
            "incident":
                True,
            "severity":
                "HIGH"
        }

    return {
        "incident":
            False,
        "severity":
            "NORMAL"
    }
