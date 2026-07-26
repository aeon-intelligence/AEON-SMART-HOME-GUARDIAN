"""
Workflow Execution Runner
"""


class WorkflowRunner:

    def run(self, workflow: dict):

        return {
            "workflow": workflow,
            "execution": "STARTED",
            "monitoring": True
        }
