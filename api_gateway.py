from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid

from security.jwt_manager import verify_access_token
from security.permission_registry import check_permission
from security.policy_engine import evaluate_policy
from security.audit_logger import write_audit


app = FastAPI(
    title="AEON MATRIX API Gateway",
    version="2026.1.0"
)


class TelemetryEvent(BaseModel):
    event_type: str
    device_id: str
    payload: dict


class AIRequest(BaseModel):
    agent: str
    command: str
    data: dict


def verify_jwt(authorization: str | None):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing JWT token"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    result = verify_access_token(token)

    if not result["valid"]:
        raise HTTPException(
            status_code=401,
            detail=result["reason"]
        )

    return result["payload"]


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


@app.post("/telemetry")
def receive_telemetry(
    event: TelemetryEvent,
    authorization: str | None = Header(default=None)
):

    user = verify_jwt(authorization)

    write_audit(
        user["sub"],
        "telemetry_upload",
        "ACCEPTED",
        "LOW"
    )

    return {
        "event_id": str(uuid.uuid4()),
        "received": True,
        "device": event.device_id
    }


@app.post("/agent/execute")
def execute_agent(
    request: AIRequest,
    authorization: str | None = Header(default=None)
):

    user = verify_jwt(authorization)

    allowed = check_permission(
        request.agent,
        request.command
    )

    if not allowed:
        write_audit(
            user["sub"],
            request.command,
            "BLOCKED",
            "HIGH"
        )

        raise HTTPException(
            status_code=403,
            detail="Permission denied"
        )


    policy = evaluate_policy(request.command)


    write_audit(
        user["sub"],
        request.command,
        "ACCEPTED",
        policy.get("risk_level","LOW")
    )


    return {
        "request_id": str(uuid.uuid4()),
        "agent": request.agent,
        "command": request.command,
        "status": "accepted",
        "governance": policy
    }
