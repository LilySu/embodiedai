from typing import Any, Literal

from pydantic import BaseModel, Field


class AgentInvokeRequest(BaseModel):
    request_type: Literal["message_relay", "match_presentation"]
    viewer_pseudo_id: str = Field(min_length=8, max_length=128)
    payload: dict[str, Any]


class AgentInvokeResponse(BaseModel):
    request_type: str
    output: dict[str, Any]
