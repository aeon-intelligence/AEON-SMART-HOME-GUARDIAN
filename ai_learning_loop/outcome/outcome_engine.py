def evaluate_outcome(decision, result):

    success = (
        result >= 80
    )

    return {
        "decision": decision,
        "outcome_score": result,
        "status":
            "SUCCESS"
            if success
            else "IMPROVE_REQUIRED"
    }
