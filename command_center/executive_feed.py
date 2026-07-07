"""
AEON MATRIX Executive Action Feed
"""


def create_action_feed(operation):

    if operation["status"] == "CRITICAL":

        action = "ESCALATE_OPERATION"

    else:

        action = "CONTINUE_MONITORING"

    return {
        "priority": operation["status"],
        "recommended_action": action
    }
