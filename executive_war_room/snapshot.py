"""
AEON MATRIX War Room Snapshot
"""


def snapshot(situation, risk, recommendation, action):

    return {
        "war_room": "ONLINE",
        "risk_visibility": risk["overall"],
        "recommendation_queue": recommendation["status"],
        "action_tracking": action["execution_monitor"]
    }
