from datetime import datetime


def save_execution(record):

    return {
        "execution_memory":
            record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
