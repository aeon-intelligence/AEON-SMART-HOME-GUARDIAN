"""
AEON MATRIX Telemetry Event Collector
"""

from datetime import datetime
import uuid


def collect_event(
    event_type,
    source,
    payload
):

    return {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "source": source,
        "payload": payload
    }
