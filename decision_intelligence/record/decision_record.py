from datetime import datetime


def create(decision):

    return {
        "record_type": "EXECUTIVE_DECISION_RECORD",
        "decision": decision,
        "timestamp": datetime.utcnow().isoformat()
    }
