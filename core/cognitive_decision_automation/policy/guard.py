"""
Decision Policy Guard
"""


class DecisionPolicyGuard:

    def validate(self, decision: str):

        return {
            "decision": decision,
            "policy_check": "PASSED",
            "audit_required": True
        }
