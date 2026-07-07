"""
AEON MATRIX Outcome Feedback Engine
"""


def evaluate_outcome(expected, actual):

    if expected == actual:
        return {
            "accuracy": 100,
            "learning": "CONFIRMED"
        }

    return {
        "accuracy": 50,
        "learning": "ADJUSTMENT_REQUIRED"
    }
