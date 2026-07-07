"""
AEON MATRIX AI Agent Permission Registry
Least Privilege Security Layer
"""

AGENT_PERMISSIONS = {

    "forecast_agent": {
        "allow": [
            "read_sales",
            "read_inventory",
            "generate_prediction"
        ],
        "deny": [
            "modify_inventory",
            "delete_data"
        ]
    },


    "guardian_agent": {
        "allow": [
            "evaluate_policy",
            "create_alert",
            "request_human_review"
        ],
        "deny": [
            "approve_financial_action",
            "delete_audit"
        ]
    },


    "telemetry_agent": {
        "allow": [
            "collect_signal",
            "publish_event"
        ],
        "deny": [
            "change_policy"
        ]
    }
}


def check_permission(agent, action):

    if agent not in AGENT_PERMISSIONS:
        return False

    permissions = AGENT_PERMISSIONS[agent]

    if action in permissions["deny"]:
        return False

    if action in permissions["allow"]:
        return True

    return False
