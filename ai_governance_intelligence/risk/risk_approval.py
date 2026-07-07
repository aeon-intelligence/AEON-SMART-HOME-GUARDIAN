def approve(risk_score):

    return {
        "risk_score": risk_score,
        "approval":
            "AUTO_APPROVED"
            if risk_score < 30
            else "HUMAN_REVIEW_REQUIRED"
    }
