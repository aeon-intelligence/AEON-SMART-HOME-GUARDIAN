from knowledge_graph.entities.entity_store import EntityStore
from knowledge_graph.relations.relation_store import RelationStore
from knowledge_graph.context.context_engine import build_context
from knowledge_graph.reasoning.reasoning_engine import ReasoningEngine


entities = EntityStore()

stock = entities.add(
    "Inventory",
    "Operational Asset"
)

demand = entities.add(
    "Demand Forecast",
    "Prediction System"
)


relation = RelationStore().connect(
    stock["name"],
    "CAUSES",
    demand["name"]
)


context = build_context(
    stock,
    relation
)


print(
    ReasoningEngine().analyze(
        relation
    )
)

print(context)
