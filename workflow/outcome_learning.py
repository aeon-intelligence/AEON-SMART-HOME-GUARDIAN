"""
AEON MATRIX Outcome Learning Layer
"""


def record_outcome(workflow_id, result):

    return {
        "workflow_id": workflow_id,
        "learning_status": "RECORDED",
        "outcome": result
    }
