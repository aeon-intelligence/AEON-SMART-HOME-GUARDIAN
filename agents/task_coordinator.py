"""
AEON MATRIX Agent Task Coordinator
"""


def assign_task(task, agents):

    return {
        "mission": task,
        "assigned_agents": agents,
        "status": "IN_PROGRESS"
    }
