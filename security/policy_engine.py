"""
AEON MATRIX Policy Engine
Governance Rule Enforcement Layer
"""

POLICIES = {

    "NO_SCAN_NO_MOVE": {
        "enabled": True,
        "risk_level": "HIGH"
    },

    "WEIGHT_VERIFICATION_REQUIRED": {
        "enabled": True,
        "risk_level": "HIGH"
    },

    "INVENTORY_ADJUSTMENT_REQUIRES_REVIEW": {
        "enabled": True,
        "risk_level": "MEDIUM"
    },

    "CUSTOMER_DATA_PROTECTION": {
        "enabled": True,
        "risk_level": "CRITICAL"
    },

    "AI_LEARNING_QUARANTINE": {
        "enabled": True,
        "risk_level": "HIGH"
    }
}


def evaluate_policy(policy_name):

    policy = POLICIES.get(policy_name)

    if not policy:
        return {
            "allowed": False,
            "reason": "UNKNOWN_POLICY"
        }

    if policy["enabled"]:
        return {
            "allowed": True,
            "risk_level": policy["risk_level"]
        }

    return {
        "allowed": False,
        "reason": "POLICY_DISABLED"
    }
