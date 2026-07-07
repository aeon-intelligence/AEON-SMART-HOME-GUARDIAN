class ConversationSession:

    def __init__(self):
        self.history = []

    def add(self, message):

        self.history.append(message)

        return self.history
