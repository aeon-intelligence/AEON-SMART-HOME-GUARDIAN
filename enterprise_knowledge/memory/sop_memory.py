class SOPMemory:

    def store(self, process, rule):

        return {
            "type": "SOP",
            "process": process,
            "rule": rule
        }
