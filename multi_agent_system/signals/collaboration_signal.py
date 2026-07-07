from datetime import datetime


def create_signal():

    return {
        "signal":
            "AGENT_COLLABORATION",
        "timestamp":
            datetime.utcnow().isoformat()
    }
