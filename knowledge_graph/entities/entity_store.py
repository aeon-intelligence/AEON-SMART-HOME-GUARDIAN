class EntityStore:

    def __init__(self):
        self.entities = []

    def add(self, name, entity_type):

        entity = {
            "name": name,
            "type": entity_type
        }

        self.entities.append(entity)

        return entity
