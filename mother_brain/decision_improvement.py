"""
AEON MATRIX Decision Improvement Layer
"""


def improve_decision(signal):

    return {
        "next_cycle": "OPTIMIZED",
        "strategy_update": signal["signal"]
    }
