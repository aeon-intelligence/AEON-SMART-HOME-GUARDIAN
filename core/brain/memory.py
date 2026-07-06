class Memory:
    def __init__(self):
        self.state = {
            "events": [],
            "last_decision": None
        }

    def add_event(self, event):
        self.state["events"].append(event)

    def set_decision(self, decision):
        self.state["last_decision"] = decision

    def get_state(self):
        return self.state

memory = Memory()
