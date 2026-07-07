from datetime import datetime


def save_command(record):

    return {
        "memory":
            "EXECUTIVE_COMMAND",
        "record":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
