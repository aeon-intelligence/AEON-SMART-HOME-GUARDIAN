from datetime import datetime


class WorkflowPlanner:

    def create_plan(self, decision):

        return {
            "workflow": "INVENTORY_RISK_RESPONSE",
            "decision": decision,
            "steps": [
                "VERIFY_STOCK",
                "ANALYZE_DEMAND",
                "REQUEST_APPROVAL",
                "EXECUTE_ACTION"
            ],
            "created_at": datetime.utcnow().isoformat()
        }
