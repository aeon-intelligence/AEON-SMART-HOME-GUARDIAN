def approval_route(priority):

    if priority["priority_level"] == "CRITICAL":

        return {
            "approval":
                "EXECUTIVE_BOARD",
            "sla_hours": 2
        }

    return {
        "approval":
            "OPERATION_MANAGER",
        "sla_hours": 24
    }
