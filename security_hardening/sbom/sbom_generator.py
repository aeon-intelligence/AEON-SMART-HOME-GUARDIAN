from datetime import datetime


def generate_sbom(components):

    return {
        "component_count":
            len(components),
        "format":
            "SBOM",
        "generated_at":
            datetime.utcnow().isoformat()
    }
