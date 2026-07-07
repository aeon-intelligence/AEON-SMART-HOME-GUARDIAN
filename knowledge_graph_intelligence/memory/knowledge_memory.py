from datetime import datetime


def save(record):

    return {
        "memory_type":
            "KNOWLEDGE_GRAPH_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
