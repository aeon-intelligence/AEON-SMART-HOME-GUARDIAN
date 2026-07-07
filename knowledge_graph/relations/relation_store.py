class RelationStore:

    def __init__(self):
        self.relations = []

    def connect(self, source, relation, target):

        link = {
            "source": source,
            "relation": relation,
            "target": target
        }

        self.relations.append(link)

        return link
