from .policy import check_policy
from .audit import log_event

def guardian_check(agent, action):

    policy = check_policy(action)

    audit = log_event(
        event=action,
        actor=agent
    )

    return {
        "agent": agent,
        "policy": policy,
        "audit": audit
    }
