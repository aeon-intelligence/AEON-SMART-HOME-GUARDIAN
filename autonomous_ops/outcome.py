"""
AEON MATRIX Enterprise Outcome Snapshot
"""


def snapshot(operation):

    return {
        "enterprise_loop": "ACTIVE",
        "operation_status": operation["status"],
        "learning": "READY"
    }
