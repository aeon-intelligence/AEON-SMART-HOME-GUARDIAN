from security_hardening.secrets.secret_scanner import scan_secrets
from security_hardening.dependencies.dependency_audit import audit_dependencies
from security_hardening.sbom.sbom_generator import generate_sbom
from security_hardening.zerotrust.policy_engine import verify_access
from security_hardening.runtime.runtime_signal import create_security_signal


print(
    scan_secrets(
        {
            "DATABASE": "SAFE"
        }
    )
)

print(
    audit_dependencies(
        [
            "fastapi",
            "pydantic"
        ]
    )
)

print(
    generate_sbom(
        [
            "Guardian AI",
            "Mother Brain"
        ]
    )
)

print(
    verify_access(
        {
            "identity": "guardian_agent",
            "authorization": True,
            "purpose": "inventory_review"
        }
    )
)

print(
    create_security_signal(
        "POLICY_VIOLATION_ATTEMPT"
    )
)
