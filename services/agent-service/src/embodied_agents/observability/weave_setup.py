from typing import Any

from embodied_agents.observability.privacy_redactor import redact_event

_WEAVE_READY = False


def setup_weave() -> None:
    global _WEAVE_READY
    try:
        import weave

        weave.init("embodied-coffee-agent-service")
        _WEAVE_READY = True
    except Exception:
        # Observability must never block privacy guardrails or request handling.
        return


def publish_redacted_event(name: str, event: dict[str, Any]) -> None:
    if not _WEAVE_READY:
        return
    try:
        import weave

        weave.publish(redact_event(event), name=name)
    except Exception:
        return
