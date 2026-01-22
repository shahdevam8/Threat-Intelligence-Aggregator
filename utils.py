import re
from datetime import datetime
import validators

def parse_iocs(row, source="local"):
    """Parse IOC dictionary"""
    value = row.get("ioc") or row.get("value") or ""
    return normalize_ioc(value, source=source)

def normalize_ioc(ioc_value, source="local"):
    ioc_value = ioc_value.strip()
    if not ioc_value:
        return None
    ioc_type = "unknown"
    if validators.ipv4(ioc_value) or validators.ipv6(ioc_value):
        ioc_type = "IP"
    elif re.match(r'^([a-fA-F0-9]{32,64})$', ioc_value):
        ioc_type = "hash"
    elif validators.domain(ioc_value):
        ioc_type = "domain"
    elif ioc_value.startswith("http"):
        ioc_type = "url"
    return {
        "value": ioc_value,
        "type": ioc_type,
        "source": source,
        "timestamp": datetime.now().isoformat(),
    }
