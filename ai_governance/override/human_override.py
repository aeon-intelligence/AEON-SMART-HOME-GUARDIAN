def request_override(reason):

    return {
        "override_required": True,
        "reason": reason,
        "approval": "HUMAN_REVIEW"
    }
