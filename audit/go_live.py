"""
AEON MATRIX Go-Live Assessment
"""


def assessment(audit):

    if audit["status"] == "READY":

        return {
            "go_live_status": "APPROVED",
            "mode": "PRODUCTION_READY"
        }

    return {
        "go_live_status": "HOLD",
        "mode": "REVIEW"
    }
