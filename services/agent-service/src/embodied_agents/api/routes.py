from fastapi import APIRouter, Depends, HTTPException

from embodied_agents.agents.triage import triage
from embodied_agents.api.auth import AuthContext, require_auth
from embodied_agents.guardrails.input import GuardrailError
from embodied_agents.observability.privacy_redactor import redact_event
from embodied_agents.schemas.agent import AgentInvokeRequest, AgentInvokeResponse

router = APIRouter()


@router.post("/v1/agents/invoke", response_model=AgentInvokeResponse)
async def invoke_agent(
    request: AgentInvokeRequest,
    auth: AuthContext = Depends(require_auth),
) -> AgentInvokeResponse:
    if auth.pseudo_id and auth.pseudo_id != request.viewer_pseudo_id:
        raise HTTPException(status_code=403, detail="jwt_binding_mismatch")

    try:
        response = await triage(request)
    except GuardrailError as exc:
        raise HTTPException(status_code=400, detail=exc.reason) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    redact_event({"request": request.model_dump(), "response": response.model_dump()})
    return response
