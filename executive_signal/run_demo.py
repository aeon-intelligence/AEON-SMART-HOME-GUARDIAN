from executive_signal.engine.signal_engine import ExecutiveSignalEngine
from executive_signal.signals.signal_store import save_signal
from executive_signal.dashboard.dashboard_feed import create_dashboard_feed


decision = {
    "decision": "ESCALATE_TO_EXECUTIVE",
    "risk_score": 91
}


engine = ExecutiveSignalEngine()

signal = engine.generate(decision)

save_signal(signal)

print(create_dashboard_feed(signal))
