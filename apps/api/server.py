from fastapi import FastAPI
from core.brain.engine import decide
from services.event_bus.bus import bus
from core.brain.memory import memory

app = FastAPI(title="AEON MATRIX LEVEL 3")

@app.get("/status")
def status():
    return {"system": "AEON LEVEL 3 ONLINE"}

@app.post("/decision")
def decision(payload: dict):
    return decide(payload)

@app.post("/event")
def event(payload: dict):
    return bus.publish(payload)

@app.get("/events")
def events():
    return bus.get_all()

@app.get("/memory")
def get_memory():
    return memory.get_state()
