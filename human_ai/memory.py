"""
AEON MATRIX Enterprise Decision Memory
"""

MEMORY = []


def store(decision):

    MEMORY.append(decision)

    return {
        "stored": True,
        "memory_records": len(MEMORY)
    }
