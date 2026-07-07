"""
AEON MATRIX AI Recommendation Queue
"""


def queue_recommendation(decision):

    return {
        "queue_status": "READY",
        "ai_action": decision["recommendations"][0],
        "requires_guardian_review":
            decision["priority"] == "HIGH"
    }
