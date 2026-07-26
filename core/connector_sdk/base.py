class BaseConnector:

    def connect(self):
        raise NotImplementedError

    def health_check(self):
        raise NotImplementedError

    def pull(self):
        raise NotImplementedError

    def push(self, payload):
        raise NotImplementedError

    def subscribe_events(self):
        raise NotImplementedError
