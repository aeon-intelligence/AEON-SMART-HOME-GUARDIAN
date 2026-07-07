class TaskRegistry:

    def __init__(self):

        self.tasks = []


    def assign(self, agent, task):

        record = {
            "agent": agent,
            "task": task,
            "status": "ASSIGNED"
        }

        self.tasks.append(record)

        return record
