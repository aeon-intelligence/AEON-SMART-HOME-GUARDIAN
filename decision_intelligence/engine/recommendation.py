from datetime import datetime


class RecommendationEngine:

    def analyze(self, signal):

        risk = signal.get("risk_score", 0)

        if risk >= 80:
            action = "ESCALATE_TO_EXECUTIVE"
        elif risk >= 50:
            action = "MONITOR_AND_OPTIMIZE"
        else:
            action = "NORMAL_OPERATION"

        return {
            "recommended_action": action,
            "risk_score": risk,
            "reason": "Generated from enterprise intelligence signal",
            "timestamp": datetime.utcnow().isoformat()
        }
