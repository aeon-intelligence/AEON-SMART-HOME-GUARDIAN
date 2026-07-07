from datetime import datetime


class AuditLogger:

    def record(self, event):

        return {
            "event": event,
            "timestamp":
                datetime.utcnow().isoformat()
        }
