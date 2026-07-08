"""
Human In The Loop Approval Layer
"""


class HITLApproval:

    def request(self, action: str):

        return {
            "action": action,
            "approval_required": True,
            "status": "PENDING"
        }
