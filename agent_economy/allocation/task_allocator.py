from datetime import datetime


class TaskAllocator:

    def allocate(self, task, agent):

        return {
            "task": task,
            "assigned_agent": agent["name"],
            "status": "ALLOCATED",
            "timestamp":
                datetime.utcnow().isoformat()
        }
