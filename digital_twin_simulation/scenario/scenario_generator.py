from datetime import datetime


class ScenarioGenerator:

    def create(self, name, variables):

        return {
            "scenario": name,
            "variables": variables,
            "created_at": datetime.utcnow().isoformat()
        }
