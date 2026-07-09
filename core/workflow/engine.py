class WorkflowEngine:
    def execute(self, workflow_name, payload):
        return {
            "workflow": workflow_name,
            "status": "completed",
            "payload": payload
        }
