"""
AEON MATRIX Model Evaluation Engine
"""


def evaluate(model_output):

    accuracy = model_output.get("accuracy", 0)

    if accuracy >= 90:
        status = "EXCELLENT"
    elif accuracy >= 75:
        status = "GOOD"
    else:
        status = "REVIEW_REQUIRED"

    return {
        "accuracy": accuracy,
        "quality_status": status
    }
