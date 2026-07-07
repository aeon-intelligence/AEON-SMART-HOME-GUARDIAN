from datetime import datetime


def collect_signal(employee_group, activity):

    return {
        "group": employee_group,
        "activity": activity,
        "timestamp":
            datetime.utcnow().isoformat()
    }
