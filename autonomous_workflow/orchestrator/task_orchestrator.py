class TaskOrchestrator:

    def execute(self, workflow):

        tasks = []

        for step in workflow["steps"]:
            tasks.append(
                {
                    "task": step,
                    "status": "PENDING"
                }
            )

        return tasks
