"""
Agent Governance Policy
"""


class AgentGovernance:

    def validate(self, action):

        return {
            "action": action,
            "policy_status": "APPROVED",
            "human_review_available": True
        }
