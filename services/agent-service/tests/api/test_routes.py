from fastapi.testclient import TestClient

from embodied_agents.api.main import app


def test_invoke_message_relay_route(monkeypatch) -> None:
    monkeypatch.setenv("AGENT_SERVICE_AUTH_DISABLED", "1")
    client = TestClient(app)

    response = client.post(
        "/v1/agents/invoke",
        json={
            "request_type": "message_relay",
            "viewer_pseudo_id": "sender_123",
            "payload": {
                "match_id": "match_123",
                "sender_pseudo_id": "sender_123",
                "recipient_pseudo_id": "recipient_123",
                "raw_text": "My email is mary@example.com",
                "match_status": "pre",
            },
        },
    )

    assert response.status_code == 200
    assert response.json()["output"]["blocked"] is False


def test_auth_required_by_default(monkeypatch) -> None:
    monkeypatch.delenv("AGENT_SERVICE_AUTH_DISABLED", raising=False)
    client = TestClient(app)

    response = client.post(
        "/v1/agents/invoke",
        json={"request_type": "message_relay", "viewer_pseudo_id": "sender_123", "payload": {}},
    )

    assert response.status_code == 401
