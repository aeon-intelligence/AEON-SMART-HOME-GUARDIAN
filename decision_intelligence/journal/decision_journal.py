import json
from datetime import datetime


def create_decision_record(signal, recommendation):

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_signal": signal,
        "decision": recommendation
    }

    with open(
        "decision_intelligence/journal/decision_history.json",
        "a"
    ) as file:
        file.write(json.dumps(record) + "\n")

    return record
