from datetime import datetime


class OutcomeTracker:

    def record(self, decision, result):

        return {
            "decision": decision,
            "actual_result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
