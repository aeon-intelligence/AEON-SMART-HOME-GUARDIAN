"""
AEON MATRIX Enterprise Knowledge Graph
"""

NODES = []


def add_entity(entity, entity_type):

    NODES.append({
        "entity": entity,
        "type": entity_type
    })

    return {
        "registered": True,
        "entity": entity
    }


def graph_status():

    return {
        "nodes": len(NODES),
        "graph": "ACTIVE"
    }
