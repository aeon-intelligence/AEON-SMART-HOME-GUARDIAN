from enterprise_knowledge_graph.entity.entity_manager import create
from enterprise_knowledge_graph.graph.relationship_graph import connect
from enterprise_knowledge_graph.reasoning.reasoning_engine import reason
from enterprise_knowledge_graph.query.knowledge_query import query
from enterprise_knowledge_graph.memory.knowledge_memory import save


warehouse = create(
    "WAREHOUSE_A",
    "LOGISTICS_NODE"
)

inventory = create(
    "INVENTORY_SYSTEM",
    "BUSINESS_SYSTEM"
)

relationship = connect(
    warehouse,
    inventory,
    "DEPENDS_ON"
)

reasoning = reason(
    relationship
)

answer = query(
    "WHY_INVENTORY_RISK_INCREASED"
)

print(warehouse)
print(inventory)
print(relationship)
print(reasoning)
print(answer)
print(save(reasoning))
