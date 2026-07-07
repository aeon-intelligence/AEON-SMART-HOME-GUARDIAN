def diagnose(agent):

    issues = []

    if agent["accuracy"] < 90:
        issues.append(
            "MODEL_ACCURACY_IMPROVEMENT"
        )

    if agent["latency"] > 500:
        issues.append(
            "PERFORMANCE_OPTIMIZATION"
        )

    return {
        "agent": agent["name"],
        "issues": issues
    }
