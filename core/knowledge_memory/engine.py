"""
AEON MATRIX Enterprise Knowledge Memory Intelligence

Capture enterprise knowledge, events and
decision history for future reasoning.
"""


class KnowledgeMemoryEngine:

    def __init__(self):
        self.memory = []

    def store_memory(
        self,
        event_type,
        content,
        source
    ):

        record = {
            "event_type": event_type,
            "content": content,
            "source": source,
            "linked": True
        }

        self.memory.append(record)

        return record

    def search_memory(
        self,
        keyword
    ):

        results = []

        for item in self.memory:
            if keyword.lower() in str(
                item["content"]
            ).lower():
                results.append(item)

        return {
            "matches": results,
            "memory_count": len(results)
        }

    def generate_learning_context(self):

        return {
            "total_memory": len(
                self.memory
            ),
            "knowledge_ready": True,
            "mother_brain_sync": True
        }
