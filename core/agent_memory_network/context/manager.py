"""
Agent Context Manager
"""


class ContextManager:

    def build(self, signals: dict):

        return {
            "context": signals,
            "ready": True
        }
