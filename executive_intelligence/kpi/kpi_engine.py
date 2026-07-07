from datetime import datetime


class KPIEngine:

    def calculate(self, operation):

        return {
            "OTIF": operation.get("otif", 0),
            "productivity": operation.get(
                "productivity",
                0
            ),
            "cost_efficiency": operation.get(
                "cost_efficiency",
                0
            ),
            "timestamp":
                datetime.utcnow().isoformat()
        }
