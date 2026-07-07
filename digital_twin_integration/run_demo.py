from digital_twin_integration.events.event_mapper import map_event
from digital_twin_integration.sync.twin_sync import TwinSyncEngine
from digital_twin_integration.executive.situation_room import create_snapshot


event = {
    "type": "STOCK_SHORTAGE"
}


signal = map_event(event)

engine = TwinSyncEngine()

state = engine.update(
    signal["mapped_signal"]
)

print(
    create_snapshot(state)
)
