from fastapi import FastAPI

from core.brain.engine import decide
from services.event_bus.bus import bus
from core.brain.memory import memory


app = FastAPI(
    title="AEON MATRIX LEVEL 3",
    description="Autonomous Intelligence Runtime",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "system": "AEON MATRIX LEVEL 3",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "online"
    }


@app.get("/brain/status")
def brain_status():
    return {
        "brain": "Mother Brain",
        "status": "ready",
        "mode": "runtime",
    }


@app.post("/decision")
def decision(payload: dict):
    return decide(payload)


@app.post("/event")
def event(payload: dict):
    return bus.publish(payload)


@app.get("/events")
def events():
    return bus.get_all()
