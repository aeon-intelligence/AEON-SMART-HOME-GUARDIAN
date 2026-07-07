"""
AEON MATRIX Audit Logger
Governance Traceability Layer
"""

from datetime import datetime
import json
import os


AUDIT_FILE = "security/audit_log.json"


def write_audit(
    actor,
    action,
    result,
    risk_level="LOW"
):

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "actor": actor,
        "action": action,
        "risk_level": risk_level,
        "result": result
    }

    os.makedirs(
        os.path.dirname(AUDIT_FILE),
        exist_ok=True
    )

    with open(AUDIT_FILE, "a") as f:
        f.write(
            json.dumps(event)
            + "\n"
        )

    return event
