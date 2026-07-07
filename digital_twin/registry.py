"""
AEON MATRIX Digital Twin Registry
"""

TWINS = {}


def register(name, data):

    TWINS[name] = data

    return {
        "registered": True,
        "twin_name": name
    }


def get_twin(name):

    return TWINS.get(name)
