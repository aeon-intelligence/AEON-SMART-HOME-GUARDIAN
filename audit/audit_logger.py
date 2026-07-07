import json
from datetime import datetime


def write_audit(record):

    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "audit_record": record
    }

    with open("audit/audit_history.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    return payload
