from embodied_agents.agents.match_presentation import run_match_presentation
from embodied_agents.agents.message_relay import run_message_relay
from embodied_agents.guardrails.input import check_invoke_binding, reject_oversize
from embodied_agents.schemas.agent import AgentInvokeRequest, AgentInvokeResponse
from embodied_agents.schemas.match import MatchPresentationInput
from embodied_agents.schemas.message import MessageInput


async def triage(request: AgentInvokeRequest) -> AgentInvokeResponse:
    reject_oversize(request.payload)
    check_invoke_binding(viewer_pseudo_id=request.viewer_pseudo_id, payload=request.payload)

    if request.request_type == "message_relay":
        output = await run_message_relay(MessageInput.model_validate(request.payload))
    elif request.request_type == "match_presentation":
        output = await run_match_presentation(MatchPresentationInput.model_validate(request.payload))
    else:
        raise ValueError("unsupported_request_type")

    return AgentInvokeResponse(request_type=request.request_type, output=output.model_dump())
