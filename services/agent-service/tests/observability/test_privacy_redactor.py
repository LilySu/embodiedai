from embodied_agents.observability.privacy_redactor import redact_event


def test_redacts_nested_sensitive_values() -> None:
    event = {
        "sender_pseudo_id": "pseudo_sender",
        "payload": {"raw_text": "Call 415-555-1212", "safe": "ok"},
    }

    redacted = redact_event(event)

    assert redacted["sender_pseudo_id"].startswith("hash:")
    assert redacted["payload"]["raw_text"] == "[redacted]"
    assert redacted["payload"]["safe"] == "ok"
