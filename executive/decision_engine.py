"""
AEON MATRIX Executive Decision Engine
"""


def create_decision_feed(kpi):

    decisions = []

    if kpi["inventory_health"] < 70:
        decisions.append(
            "INITIATE_INVENTORY_RECOVERY"
        )

    if kpi["sla_score"] < 80:
        decisions.append(
            "ESCALATE_OPERATIONAL_REVIEW"
        )

    if kpi["productivity"] < 75:
        decisions.append(
            "OPTIMIZE_WORKFLOW"
        )

    if not decisions:
        decisions.append(
            "CONTINUE_OPTIMAL_OPERATION"
        )

    return {
        "priority": "HIGH"
            if len(decisions) > 1
            else "NORMAL",
        "recommendations": decisions
    }
