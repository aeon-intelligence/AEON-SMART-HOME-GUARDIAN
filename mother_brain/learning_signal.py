"""
AEON MATRIX Learning Signal Generator
"""


def generate_learning_signal(outcome):

    if outcome["accuracy"] >= 90:
        signal = "REINFORCE_PATTERN"

    else:
        signal = "UPDATE_STRATEGY"

    return {
        "signal": signal,
        "learning_ready": True
    }
