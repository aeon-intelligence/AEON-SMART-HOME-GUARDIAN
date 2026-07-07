from datetime import datetime


class ImpactAnalyzer:

    def analyze(self, context):

        risk = context.get(
            "risk_score",
            0
        )

        return {
            "impact_level":
                "HIGH"
                if risk >= 80
                else "NORMAL",

            "affected_area": [
                "Operations",
                "Customer Service",
                "Finance"
            ],

            "timestamp":
                datetime.utcnow().isoformat()
        }
