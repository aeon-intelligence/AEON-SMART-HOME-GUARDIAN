"""
Runtime Context Memory
"""


class RuntimeMemory:

    def store(self, event: dict):

        return {
            "stored": True,
            "event": event
        }
