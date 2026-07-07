"""
AEON MATRIX Execution Queue
"""


QUEUE = []


def enqueue_workflow(workflow):

    QUEUE.append(workflow)

    return {
        "queued": True,
        "queue_size": len(QUEUE),
        "workflow_status": workflow["status"]
    }
