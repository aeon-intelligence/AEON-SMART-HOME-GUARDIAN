from datetime import datetime


class WorkflowEngine:

    def __init__(self):
        self.workflows = []


    def create(self, trigger, action):

        workflow = {
            "trigger": trigger,
            "action": action,
            "status": "CREATED",
            "timestamp": datetime.utcnow().isoformat()
        }

        self.workflows.append(workflow)

        return workflow


    def list_workflows(self):

        return self.workflows
