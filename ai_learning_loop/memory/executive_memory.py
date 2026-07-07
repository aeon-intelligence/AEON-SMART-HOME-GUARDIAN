from datetime import datetime


def save_learning(strategy):

    return {
        "memory_type":
            "EXECUTIVE_LEARNING",
        "record":
            strategy,
        "timestamp":
            datetime.utcnow().isoformat()
    }
