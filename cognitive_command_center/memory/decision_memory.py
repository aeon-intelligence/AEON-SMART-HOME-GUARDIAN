from datetime import datetime


def save(decision):

    return {
        "memory_type":
            "EXECUTIVE_DECISION_MEMORY",
        "decision": decision,
        "timestamp":
            datetime.utcnow().isoformat()
    }
