class AIConstitution:

    def __init__(self):

        self.rules = [
            "EXPLAIN_DECISIONS",
            "PROTECT_DATA",
            "REQUIRE_APPROVAL_FOR_HIGH_RISK"
        ]

    def validate(self, action):

        return {
            "action": action,
            "rules_checked": self.rules,
            "status": "VALIDATED"
        }
