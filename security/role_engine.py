"""
AEON MATRIX RBAC Role Engine
Role Based Access Control Layer
"""

ROLES = {

    "warehouse_operator": {
        "allow": [
            "scan_item",
            "confirm_pick",
            "view_inventory"
        ]
    },

    "warehouse_supervisor": {
        "allow": [
            "approve_adjustment",
            "review_exception",
            "view_inventory"
        ]
    },

    "executive": {
        "allow": [
            "view_dashboard",
            "approve_strategy",
            "view_analytics"
        ]
    },

    "ai_agent": {
        "allow": [
            "generate_prediction",
            "create_alert",
            "request_review"
        ]
    }
}


def check_role_permission(role, action):

    role_data = ROLES.get(role)

    if not role_data:
        return False

    return action in role_data["allow"]
