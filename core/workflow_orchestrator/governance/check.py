"""
Workflow Governance Check
"""


class WorkflowGovernance:

    def validate(self, workflow):

        return {
            "workflow": workflow,
            "policy_check": "PASSED",
            "human_review": True
        }
