"""
AEON MATRIX Outcome Recorder
"""

MEMORY = []


def record(outcome):

    MEMORY.append(outcome)

    return {
        "recorded": True,
        "memory_size": len(MEMORY)
    }
