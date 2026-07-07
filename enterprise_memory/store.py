"""
AEON MATRIX Enterprise Memory Store
"""

MEMORY = []


def save(event):

    MEMORY.append(event)

    return {
        "memory_status": "ACTIVE",
        "records": len(MEMORY)
    }
