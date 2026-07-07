"""
AEON MATRIX Audit Logger
Governance Traceability Layer
"""

from datetime import datetime
import json
import os

AUDIT_FILE = "security/audit_log.json"


def write_audit(actor, action, result, risk_level="LOW"):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "actor": actor,
        "action": action,
        "risk_level": risk_level,
        "result": result
    }

    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    return event


def read_audit():
    if not os.path.exists(AUDIT_FILE):
        return []

    with open(AUDIT_FILE, "r") as f:
        return [
            json.loads(line)
            for line in f.readlines()
        ]
