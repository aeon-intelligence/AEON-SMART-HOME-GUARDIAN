class ActionQueue:

    def __init__(self):
        self.queue = []

    def add(self, task):

        self.queue.append(task)

        return self.queue
