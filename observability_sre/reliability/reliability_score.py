def calculate_score(metrics):

    score = 100

    if metrics["latency_ms"] > 300:
        score -= 20

    return {
        "reliability_score": score
    }
