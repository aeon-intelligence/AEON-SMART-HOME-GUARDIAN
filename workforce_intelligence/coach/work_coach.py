from datetime import datetime


class AIWorkCoach:

    def analyze(self, employee_signal):

        gap = employee_signal.get(
            "skill_gap",
            "unknown"
        )

        if gap == "AI_OPERATION":
            recommendation = "Complete AI workflow training"
        else:
            recommendation = "Continue standard learning path"

        return {
            "coach": "AEON AI Work Coach",
            "skill_gap": gap,
            "recommendation": recommendation,
            "timestamp": datetime.utcnow().isoformat()
        }
