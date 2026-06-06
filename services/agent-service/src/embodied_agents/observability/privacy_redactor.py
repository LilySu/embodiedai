import hashlib
from typing import Any

SENSITIVE_KEYS = {
    "raw_text",
    "scrubbed_text",
    "candidate_bio",
    "bio",
    "message",
    "sender_pseudo_id",
    "recipient_pseudo_id",
    "viewer_pseudo_id",
    "candidate_pseudo_id",
}


def redact_event(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _redact_key_value(key, item) for key, item in value.items()}
    if isinstance(value, list):
        return [redact_event(item) for item in value]
    return value


def _redact_key_value(key: str, value: Any) -> Any:
    if key.endswith("_pseudo_id") and isinstance(value, str):
        return f"hash:{hashlib.sha256(value.encode()).hexdigest()[:12]}"
    if key in SENSITIVE_KEYS:
        return "[redacted]"
    return redact_event(value)
