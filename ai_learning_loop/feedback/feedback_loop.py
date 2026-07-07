def learn_from_feedback(outcome):

    return {
        "learning_signal":
            outcome["status"],
        "adjustment":
            "OPTIMIZE_MODEL"
            if outcome["status"] != "SUCCESS"
            else "REINFORCE_PATTERN"
    }
