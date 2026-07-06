from fastapi import FastAPI, Request, HTTPException
import time
import hashlib

app = FastAPI(title="AEON API GATEWAY")

# =========================
# Simple in-memory security layer
# =========================
VALID_TOKENS = {
    "SMART_HOME_DEVICE_01": "secure-token-123"
}

# =========================
# Audit Log
# =========================
audit_log = []

# =========================
# Security Check
# =========================
def verify_token(device_id, token):
    if device_id not in VALID_TOKENS:
        return False
    return VALID_TOKENS[device_id] == token

# =========================
# Data Sanitizer (CRITICAL)
# =========================
def sanitize_event(event: dict):
    # NEVER allow raw media fields
    blocked_fields = ["video", "audio", "image", "frame", "raw_stream"]

    clean = {}
    for k, v in event.items():
        if k in blocked_fields:
            continue
        clean[k] = v

    return clean

# =========================
# Forward to AEON MATRIX (mock)
# =========================
def forward_to_matrix(event):
    print("🚀 Forwarding to AEON MATRIX:", event)
    return {
        "status": "forwarded",
        "timestamp": time.time()
    }

# =========================
# MAIN ENDPOINT
# =========================
@app.post("/event")
async def receive_event(request: Request):

    data = await request.json()

    device_id = data.get("device_id")
    token = data.get("token")
    event = data.get("event")

    # 1. Security check
    if not verify_token(device_id, token):
        raise HTTPException(status_code=403, detail="Unauthorized device")

    # 2. Sanitize
    clean_event = sanitize_event(event)

    # 3. Audit log
    audit_log.append({
        "device": device_id,
        "event": clean_event,
        "time": time.time()
    })

    # 4. Forward
    result = forward_to_matrix(clean_event)

    return {
        "status": "ok",
        "gateway": "AEON_API_GATEWAY",
        "processed_event": clean_event,
        "matrix_response": result
    }

# =========================
# LOG VIEW
# =========================
@app.get("/audit")
def get_audit_log():
    return audit_log
