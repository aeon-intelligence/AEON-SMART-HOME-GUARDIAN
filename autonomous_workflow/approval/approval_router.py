def route_approval(risk_score):

    if risk_score >= 80:
        return {
            "approval_required": True,
            "approver": "EXECUTIVE"
        }

    return {
        "approval_required": False,
        "approver": "SYSTEM"
    }
