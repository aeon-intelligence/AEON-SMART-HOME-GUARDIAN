from datetime import datetime


def create(data):

    return {
        "report_type": "EXECUTIVE_COMMAND_REPORT",
        "data": data,
        "timestamp": datetime.utcnow().isoformat()
    }
