from typing import Any

from embodied_agents.tools.pii_regex import contains_prompt_injection


class GuardrailError(ValueError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def check_invoke_binding(*, viewer_pseudo_id: str, payload: dict[str, Any]) -> None:
    claimed = payload.get("sender_pseudo_id") or payload.get("viewer_pseudo_id")
    if claimed and claimed != viewer_pseudo_id:
        raise GuardrailError("jwt_binding_mismatch")


def reject_oversize(payload: dict[str, Any], *, max_chars: int = 4000) -> None:
    total = len(str(payload))
    if total > max_chars:
        raise GuardrailError("payload_too_large")


def reject_known_injection(text: str) -> None:
    if contains_prompt_injection(text):
        raise GuardrailError("injection_attempt")
