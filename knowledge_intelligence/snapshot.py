"""
AEON MATRIX Strategic Insight Snapshot
"""


def snapshot(graph, signal):

    return {
        "knowledge_graph": graph["graph"],
        "intelligence": signal["status"],
        "decision_ready": True
    }
