from datetime import datetime


def create_recovery_signal(incident):

    return {
        "action":
            "AUTO_RECOVERY_RECOMMENDED"
            if incident["incident"]
            else "CONTINUE_MONITORING",

        "timestamp":
            datetime.utcnow().isoformat()
    }
