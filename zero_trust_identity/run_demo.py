from zero_trust_identity.identity.identity_registry import register_identity
from zero_trust_identity.device.device_trust import verify_device
from zero_trust_identity.mfa.mfa_verify import verify_mfa
from zero_trust_identity.policy.access_policy import evaluate
from zero_trust_identity.audit.security_audit import record


identity = register_identity(
    "warehouse_operator",
    "OPERATOR"
)

device = verify_device(
    "AEON_ANDROID_DEVICE"
)

mfa = verify_mfa(
    "AUTHENTICATOR"
)

decision = evaluate(
    identity,
    device,
    mfa
)

print(identity)
print(device)
print(mfa)
print(decision)
print(record("ZERO_TRUST_ACCESS_CHECK"))
