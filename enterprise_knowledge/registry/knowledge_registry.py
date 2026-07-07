from datetime import datetime


class KnowledgeRegistry:

    def __init__(self):
        self.items = []

    def register(self, title, category, content):

        record = {
            "title": title,
            "category": category,
            "content": content,
            "created_at": datetime.utcnow().isoformat()
        }

        self.items.append(record)

        return record
