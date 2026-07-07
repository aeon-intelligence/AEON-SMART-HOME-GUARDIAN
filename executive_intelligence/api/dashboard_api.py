from executive_intelligence.kpi.kpi_engine import KPIEngine
from executive_intelligence.risk.risk_heatmap import generate_heatmap
from executive_intelligence.timeline.decision_timeline import add_decision


def executive_view():

    return {

        "kpi":
            KPIEngine().calculate(
                {
                    "otif": 96,
                    "productivity": 91,
                    "cost_efficiency": 88
                }
            ),

        "risk":
            generate_heatmap(
                [
                    {
                        "area": "Inventory",
                        "risk": 91
                    }
                ]
            ),

        "timeline":
            add_decision(
                "Inventory optimization approved"
            )
    }


if __name__ == "__main__":
    print(executive_view())
