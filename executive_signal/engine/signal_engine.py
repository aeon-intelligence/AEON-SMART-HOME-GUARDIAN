from datetime import datetime


class ExecutiveSignalEngine:

    def generate(self, decision):

        risk = decision.get("risk_score", 0)

        if risk >= 80:
            priority = "CRITICAL"
        elif risk >= 50:
            priority = "HIGH"
        else:
            priority = "NORMAL"

        return {
            "signal_type": "EXECUTIVE_INTELLIGENCE_SIGNAL",
            "priority": priority,
            "risk_score": risk,
            "business_impact": {
                "operation": "INVENTORY",
                "financial_risk": risk,
                "customer_service_risk": risk
            },
            "created_at": datetime.utcnow().isoformat()
        }
