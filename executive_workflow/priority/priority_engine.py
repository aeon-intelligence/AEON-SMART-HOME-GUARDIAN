def calculate_priority(risk_score, business_impact):

    score = (
        risk_score * 0.6
        +
        business_impact * 0.4
    )

    if score >= 80:
        level = "CRITICAL"
    elif score >= 50:
        level = "HIGH"
    else:
        level = "NORMAL"

    return {
        "priority_score": score,
        "priority_level": level
    }
