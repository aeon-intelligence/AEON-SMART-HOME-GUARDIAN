from datetime import datetime


class AIAvatar:

    def __init__(self, name="AEON Assistant"):
        self.name = name

    def respond(self, question, knowledge):

        answer = "Knowledge not found"

        for item in knowledge:
            if any(
                word.lower() in str(item).lower()
                for word in question.split()
            ):
                answer = item
                break

        return {
            "assistant": self.name,
            "answer": answer,
            "timestamp": datetime.utcnow().isoformat()
        }
