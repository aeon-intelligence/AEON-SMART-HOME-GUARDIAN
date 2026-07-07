from datetime import datetime


def save_prediction(result):

    return {
        "memory_type":
            "FUTURE_INSIGHT",
        "data": result,
        "timestamp":
            datetime.utcnow().isoformat()
    }
