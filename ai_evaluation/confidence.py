"""
AEON MATRIX AI Confidence Engine
"""


def score(evaluation):

    return {
        "confidence_score": evaluation["accuracy"],
        "decision_ready":
            evaluation["accuracy"] >= 80
    }
