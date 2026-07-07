def evaluate_policy(request):

    risk = request.get(
        "risk_score",
        0
    )

    if risk >= 80:

        return {
            "decision":
                "REQUIRE_HUMAN_APPROVAL",
            "risk":
                "HIGH"
        }

    return {
        "decision":
            "AUTO_ALLOWED",
        "risk":
            "NORMAL"
    }
