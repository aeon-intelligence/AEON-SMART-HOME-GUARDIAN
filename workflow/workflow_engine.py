"""
AEON MATRIX Autonomous Workflow Engine
"""

from datetime import datetime
import uuid


def create_workflow(trigger, action, risk_level):

    return {
        "workflow_id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "trigger": trigger,
        "action": action,
        "risk_level": risk_level,
        "status": "PLANNED"
    }


def approval_gate(workflow):

    if workflow["risk_level"] == "HIGH":
        workflow["approval"] = "GUARDIAN_REQUIRED"
        workflow["status"] = "WAITING_APPROVAL"

    else:
        workflow["approval"] = "AUTO_APPROVED"
        workflow["status"] = "READY_EXECUTION"

    return workflow
