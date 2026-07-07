def calculate_confidence(data):

    score = (
        data["accuracy"]
        +
        data["simulation"]
    ) / 2

    return {
        "confidence_score": score
    }
