def check_health(agent):

    return {
        "agent": agent["agent"],
        "health":
            "GOOD"
            if agent["status"] == "ACTIVE"
            else "OFFLINE"
    }
