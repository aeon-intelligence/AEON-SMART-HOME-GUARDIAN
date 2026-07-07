from cognitive_memory.event_memory.event_store import store as store_event
from cognitive_memory.decision_memory.decision_store import store as store_decision
from cognitive_memory.outcome_memory.outcome_store import store as store_outcome
from cognitive_memory.retrieval.context_retriever import retrieve
from cognitive_memory.memory_store.memory_engine import save


event = store_event(
    {
        "type": "INVENTORY_RISK",
        "value": 91
    }
)


decision = store_decision(
    {
        "action": "OPTIMIZE_ALLOCATION"
    }
)


outcome = store_outcome(
    {
        "result": "SUCCESS"
    }
)


context = retrieve(
    "previous inventory decisions"
)


memory = save(
    {
        "event": event,
        "decision": decision,
        "outcome": outcome,
        "context": context
    }
)


print(event)
print(decision)
print(outcome)
print(context)
print(memory)
