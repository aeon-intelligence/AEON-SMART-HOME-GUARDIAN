from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid


app = FastAPI(
    title="AEON MATRIX API Gateway",
    version="2026.1.0"
)


# =========================
# Security Layer (Basic)
# =========================

API_KEY = "AEON-MATRIX-DEVICE-KEY"


def verify_device(x_api_key: str | None):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized device"
        )


# =========================
# Data Models
# =========================

class TelemetryEvent(BaseModel):
    event_type: str
    device_id: str
    payload: dict


class AIRequest(BaseModel):
    agent: str
    command: str
    data: dict


# =========================
# Health Check
# =========================

@app.get("/")
def root():
    return {
        "system": "AEON MATRIX",
        "module": "API Gateway",
        "status": "ONLINE",
        "timestamp": datetime.utcnow()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "api_gateway"
    }


# =========================
# Telemetry Ingestion
# =========================

@app.post("/telemetry")
def receive_telemetry(
    event: TelemetryEvent,
    x_api_key: str | None = Header(default=None)
):
    verify_device(x_api_key)

    return {
        "event_id": str(uuid.uuid4()),
        "received": True,
        "event_type": event.event_type,
        "device": event.device_id,
        "timestamp": datetime.utcnow()
    }


# =========================
# AI Agent Gateway
# =========================

@app.post("/agent/execute")
def execute_agent(
    request: AIRequest,
    x_api_key: str | None = Header(default=None)
):
    verify_device(x_api_key)

    return {
        "request_id": str(uuid.uuid4()),
        "agent": request.agent,
        "command": request.command,
        "status": "accepted",
        "governance": "PASSED"
    }
