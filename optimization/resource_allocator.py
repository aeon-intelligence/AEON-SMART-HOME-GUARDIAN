"""
AEON MATRIX Resource Allocation Engine
"""


def allocate_resources(priority):

    if priority == "HIGH":

        return {
            "allocation": "EXPEDITE_RESOURCES",
            "priority": priority
        }

    return {
        "allocation": "NORMAL_FLOW",
        "priority": priority
    }
