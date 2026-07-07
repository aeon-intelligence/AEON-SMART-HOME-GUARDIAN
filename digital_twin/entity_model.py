"""
AEON MATRIX Digital Twin Entity Model
"""


def create_entity(entity_id, entity_type, state):

    return {
        "entity_id": entity_id,
        "entity_type": entity_type,
        "state": state
    }
