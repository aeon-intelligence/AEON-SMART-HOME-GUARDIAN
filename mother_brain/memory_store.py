"""
AEON MATRIX Executive Memory Store
"""

from datetime import datetime
import uuid

MEMORY = []


def store_memory(event_type, data):

    record = {
        "memory_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "data": data
    }

    MEMORY.append(record)

    return record


def get_memory_count():

    return len(MEMORY)
