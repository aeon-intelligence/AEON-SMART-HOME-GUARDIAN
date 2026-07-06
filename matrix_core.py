from fastapi import FastAPI, Request
import time

app = FastAPI(title="AEON MATRIX CORE (Mother Brain)")

# =========================
# Decision Engine Logic
# =========================
def evaluate_event(event: dict):
    """
    สมองกลตัดสินใจตาม Context ของ Event ที่ถูก Clean มาแล้ว
    """
    event_type = event.get("type")
    location = event.get("location")
    confidence = event.get("confidence", 0.0)

    # 🟢 Scenario 1: มั่นใจสูงมากว่าเจอคนในบ้าน
    if event_type == "PERSON_DETECTED" and confidence >= 0.90:
        return {
            "action": "TRIGGER_SCENE",
            "scene_name": "WELCOME_HOME",
            "commands": [
                {"device": f"{location}_lights", "state": "ON", "brightness": 100},
                {"device": "hvac_system", "state": "ON", "temp": 24},
                {"device": "smart_speaker", "play": "greeting_message"}
            ],
            "threat_level": "LOW",
            "priority": "HIGH"
        }
    
    # 🟡 Scenario 2: ตรวจพบความเคลื่อนไหวแต่มั่นใจต่ำ (อาจเป็นสัตว์เลี้ยงหรือเงา)
    elif event_type == "PERSON_DETECTED" and confidence < 0.90:
         return {
            "action": "MONITOR",
            "commands": [
                {"device": f"{location}_camera", "command": "INCREASE_FRAMERATE"}
            ],
            "threat_level": "ELEVATED",
            "priority": "MEDIUM"
        }

    # ⚪ Scenario 3: Event อื่นๆ ทั่วไป
    return {
        "action": "LOG_ONLY",
        "commands": [],
        "threat_level": "NONE",
        "priority": "LOW"
    }

# =========================
# MATRIX RECEIVER ENDPOINT
# =========================
@app.post("/matrix/process")
async def process_core_event(request: Request):
    # รับ Payload ที่ถูก Sanitize มาจาก API Gateway
    data = await request.json()
    
    print(f"🧠 [AEON MATRIX] Ingesting Clean Event: {data}")
    
    # ส่งเข้าสมองกลประมวลผล
    decision = evaluate_event(data)
    
    response_payload = {
        "status": "decision_made",
        "core": "AEON_MATRIX",
        "decision": decision,
        "processed_at": time.time()
    }
    
    print(f"⚡ [AEON MATRIX] Action Dispatched: {decision['action']}")
    
    return response_payload

