"""
AEON MATRIX Final Audit Report
"""


def generate_report(audit, live):

    return {
        "system": "AEON MATRIX",
        "audit_status": audit["status"],
        "go_live": live["go_live_status"],
        "production_mode": live["mode"]
    }
