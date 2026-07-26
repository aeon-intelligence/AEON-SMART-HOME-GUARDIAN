from core.replay_engine.service import ReplayEngine

def test_replay():
    result = ReplayEngine().replay([{}, {}])
    assert result["replayed"] == 2
