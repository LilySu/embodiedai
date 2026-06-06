# Embodied Coffee

Phase 1 scaffold for Embodied Coffee: an Expo + React Native Web user app, small Next.js admin app, Supabase backend, and a Python FastAPI agent service that acts as the PII firewall for message relay and match-card presentation.

The runnable code in this repository today is the Python agent service under `services/agent-service`. The app, admin, Supabase, and docs folders define the locked MVP architecture and contracts for the next implementation passes.

## Agent Service

```bash
uv sync --extra dev
uv run pytest
uv run uvicorn embodied_agents.api.main:app --app-dir services/agent-service/src --reload
```

Primary endpoint:

```text
POST /v1/agents/invoke
```

Supported `request_type` values:

- `message_relay`
- `match_presentation`

The current implementation keeps deterministic guardrails and PII scanning local so tests can run without OpenAI credentials. The OpenAI Agents SDK integration point is isolated in `services/agent-service/src/embodied_agents/agents/runner.py`.
