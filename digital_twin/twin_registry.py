"""
AEON MATRIX Digital Twin Registry
"""

TWINS = []


def register_twin(twin):

    TWINS.append(twin)

    return {
        "registered": True,
        "total_twins": len(TWINS)
    }
