"""
Workflow Planning Layer
"""


class WorkflowPlanner:

    def plan(self, objective: str):

        return {
            "objective": objective,
            "steps": [
                "ANALYZE",
                "APPROVE",
                "EXECUTE",
                "MEASURE"
            ]
        }
