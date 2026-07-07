def calculate_adoption(usage):

    return {
        "adoption_score": usage,
        "status":
            "ACTIVE"
            if usage >= 80
            else "TRAINING_REQUIRED"
    }
