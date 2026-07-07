from datetime import datetime


class GuardianAI:

    def __init__(self):
        self.name = "AEON Guardian AI"

    def evaluate(self, event):
        risk = event.get("risk_score", 0)

        if risk >= 80:
            decision = "HUMAN_APPROVAL_REQUIRED"
        else:
            decision = "AUTO_APPROVED"

        return {
            "guardian": self.name,
            "decision": decision,
            "risk_score": risk,
            "timestamp": datetime.utcnow().isoformat()
        }
