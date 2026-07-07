"""
AEON MATRIX Executive Value Snapshot
"""


def snapshot(result, roi):

    return {
        "business_optimization": result["optimization_status"],
        "value_engine": roi["value_tracking"],
        "status": "READY"
    }
