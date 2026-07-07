"""
AEON MATRIX Cognitive Dashboard Core
"""


def build(feed, alerts):

    return {
        "dashboard": "ONLINE",
        "decision_stream": feed["status"],
        "alert_monitoring": "ACTIVE"
    }
