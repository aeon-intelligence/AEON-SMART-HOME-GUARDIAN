def optimize(agent):

    return {
        "agent": agent["name"],
        "recommended_capacity":
            min(agent["capacity"] + 10, 100),
        "optimization":
            "BALANCED"
    }
