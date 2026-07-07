def calculate(score):

    return {
        "reliability_score": score,
        "grade":
            "A"
            if score >= 90
            else "B"
    }
