from datetime import datetime


def save(record):

    return {
        "memory_type":
            "CUSTOMER_MARKET_MEMORY",
        "record": record,
        "timestamp":
            datetime.utcnow().isoformat()
    }
