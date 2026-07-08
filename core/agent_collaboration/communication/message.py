"""
Agent Communication Layer
"""


class AgentMessage:

    def send(self, source: str, target: str, message: dict):

        return {
            "from": source,
            "to": target,
            "message": message,
            "delivered": True
        }
