from core.orchestrator.engine import AIOrchestrator
from core.decision_engine.engine import DecisionEngine

def run(order):
    orchestrator = AIOrchestrator()
    decision = DecisionEngine()

    flow = orchestrator.execute(order)
    result = decision.evaluate(flow)

    print({
        "order": order,
        "workflow": flow,
        "decision": result,
        "status": "SIMULATION_COMPLETE"
    })

if __name__ == "__main__":
    run({"order_id":"SIM-1001"})
