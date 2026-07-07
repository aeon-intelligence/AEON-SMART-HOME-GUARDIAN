from datetime import datetime


def save_interaction(data):

    return {
        "memory_type":
            "AVATAR_INTERACTION",
        "data": data,
        "timestamp":
            datetime.utcnow().isoformat()
    }
