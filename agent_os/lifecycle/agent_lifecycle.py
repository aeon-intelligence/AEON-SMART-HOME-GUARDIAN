from datetime import datetime


class AgentLifecycle:

    def create(self, name, role):

        return {
            "agent": name,
            "role": role,
            "status": "ACTIVE",
            "created_at":
                datetime.utcnow().isoformat()
        }

    def shutdown(self, agent):

        agent["status"] = "INACTIVE"

        return agent
