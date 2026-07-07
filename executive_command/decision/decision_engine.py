from datetime import datetime


def create_decision(signal, recommendation):

    return {
        "signal": signal,
        "decision": recommendation,
        "created_at":
            datetime.utcnow().isoformat()
    }
