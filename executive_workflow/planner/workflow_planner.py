from datetime import datetime


def create_workflow(action, approval):

    return {
        "action": action,
        "approval_path": approval,
        "created_at":
            datetime.utcnow().isoformat()
    }
