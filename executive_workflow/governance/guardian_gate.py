def guardian_validate(action):

    blocked_actions = [
        "DELETE_DATA",
        "BYPASS_POLICY"
    ]

    if action in blocked_actions:

        return {
            "status": "REJECTED",
            "reason":
                "Policy violation"
        }

    return {
        "status": "APPROVED",
        "reason":
            "Governance passed"
    }
