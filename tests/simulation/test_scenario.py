from core.scenario_engine.service import ScenarioEngine

def test_compare():
    result = ScenarioEngine().compare([{}, {}])
    assert result["evaluated"] == 2
