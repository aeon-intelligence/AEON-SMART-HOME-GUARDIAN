from datetime import datetime


def track_outcome(decision, result):

    return {
        "decision": decision,
        "actual_result": result,
        "learning_timestamp": datetime.utcnow().isoformat()
    }
