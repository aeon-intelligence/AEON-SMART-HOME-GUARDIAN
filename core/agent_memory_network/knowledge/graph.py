"""
Knowledge Relationship Layer
"""


class KnowledgeGraphConnector:

    def link(self, knowledge: dict):

        return {
            "knowledge_linked": True,
            "entity": knowledge
        }
