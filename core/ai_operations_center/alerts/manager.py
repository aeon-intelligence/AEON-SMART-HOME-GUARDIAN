"""
AI Operations Alert Manager
"""


class AlertManager:

    def register(self, alert):

        return {
            "alert": alert,
            "recorded": True,
            "audit_required": True
        }
