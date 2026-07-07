from governance.guardian_ai.guardian import GuardianAI
from audit.audit_logger import write_audit


def run_guardian_test():

    event = {
        "event_type": "INVENTORY_RISK_SIGNAL",
        "risk_score": 91
    }

    guardian = GuardianAI()

    decision = guardian.evaluate(event)

    return write_audit(decision)


if __name__ == "__main__":
    print(run_guardian_test())
