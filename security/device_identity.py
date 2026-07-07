"""
AEON MATRIX Device Identity Layer
Zero Trust Device Verification
"""

DEVICES = {
    "WMS-HH-001": {
        "type": "ANDROID_SCANNER",
        "trust_level": "VERIFIED",
        "status": "ACTIVE"
    }
}


def verify_device(device_id):

    device = DEVICES.get(device_id)

    if not device:
        return {
            "verified": False,
            "reason": "UNKNOWN_DEVICE"
        }

    if device["status"] != "ACTIVE":
        return {
            "verified": False,
            "reason": "DEVICE_DISABLED"
        }

    return {
        "verified": True,
        "device": device
    }
