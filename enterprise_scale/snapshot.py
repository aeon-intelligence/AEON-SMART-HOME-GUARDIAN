"""
AEON MATRIX Enterprise Scale Snapshot
"""


def snapshot(tenant, warehouse, regional):

    return {
        "enterprise_scale": "ACTIVE",
        "tenant_layer": tenant["tenant_status"],
        "warehouse_network": warehouse["network_status"],
        "regional_control": regional["command_status"]
    }
