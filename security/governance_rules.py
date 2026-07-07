"""
AEON MATRIX Human-in-the-loop Governance Rules
"""

HIGH_RISK_ACTIONS = [
    "inventory_adjustment",
    "financial_approval",
    "policy_change"
]


def require_human_review(action):

    if action in HIGH_RISK_ACTIONS:
        return {
            "required": True,
            "reason": "HIGH_RISK_ACTION"
        }

    return {
        "required": False,
        "reason": "AUTO_APPROVED"
    }
