from datetime import datetime


class KnowledgeRegistry:

    def __init__(self):
        self.knowledge = []


    def add(self, title, category, content):

        record = {
            "title": title,
            "category": category,
            "content": content,
            "created_at":
                datetime.utcnow().isoformat()
        }

        self.knowledge.append(record)

        return record
