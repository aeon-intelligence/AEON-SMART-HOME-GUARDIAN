from identity_federation.identity.federation import authenticate
from identity_federation.secrets.secrets_manager import get_secret
from identity_federation.certificate.certificate_manager import validate
from identity_federation.key_management.key_manager import rotate
from identity_federation.memory.identity_memory import save


identity = authenticate("warehouse_operator")

secret = get_secret("WMS_API_KEY")

certificate = validate("DEVICE_CERTIFICATE")

key = rotate("MASTER_KEY")

memory = save({
    "identity": identity,
    "secret": secret,
    "certificate": certificate,
    "key": key,
})

print(identity)
print("***REDACTED_SECRET***")
print(certificate)
print("***REDACTED_KEY***")

print({
    **memory,
    "record": {
        **memory["record"],
        "secret": "***REDACTED***",
        "key": "***REDACTED***",
    },
})
