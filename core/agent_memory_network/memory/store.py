"""
Agent Memory Storage Layer
"""


class MemoryStore:

    def save(self, event: dict):

        return {
            "stored": True,
            "event": event
        }
