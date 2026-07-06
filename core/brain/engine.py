from services.forecast.engine import forecast_demand
from core.brain.memory import memory

def decide(payload: dict):

    stock = payload.get("stock_level", 100)
    demand = payload.get("demand", 50)
    waste = payload.get("waste_risk", 0)

    forecast = forecast_demand(demand, 0.25)

    event_pressure = len(memory.state["events"]) * 2

    risk = (
        (100 - stock) * 0.4 +
        waste * 0.3 +
        forecast["risk"] * 0.3 +
        event_pressure
    )

    if risk > 70:
        action = "urgent_restock"
    elif risk > 40:
        action = "prepare_order"
    else:
        action = "normal_operation"

    decision = {
        "risk_score": round(risk, 2),
        "action": action,
        "forecast": forecast,
        "memory_events": len(memory.state["events"])
    }

    memory.set_decision(decision)

    return decision
