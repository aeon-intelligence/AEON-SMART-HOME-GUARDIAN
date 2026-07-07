def grant_permission(agent, capability):

    return {
        "agent": agent,
        "permission": capability,
        "policy": "GUARDIAN_VALIDATED"
    }
