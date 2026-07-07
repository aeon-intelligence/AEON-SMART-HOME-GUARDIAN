from datetime import datetime


class ReflectionEngine:

    def analyze(self, outcome):

        if outcome["actual_result"] == "SUCCESS":
            insight = "Decision pattern validated"
        else:
            insight = "Decision requires optimization"

        return {
            "reflection": insight,
            "timestamp": datetime.utcnow().isoformat()
        }
