from typing import Literal

from pydantic import BaseModel, Field


class RemovedItem(BaseModel):
    kind: str
    value: str


class MessageInput(BaseModel):
    sender_pseudo_id: str = Field(min_length=8, max_length=128)
    recipient_pseudo_id: str = Field(min_length=8, max_length=128)
    raw_text: str = Field(min_length=1, max_length=2000)
    match_status: Literal["pre", "post"]
    post_match_contact_consent: bool = False


class MessageOutput(BaseModel):
    scrubbed_text: str = ""
    removed: list[RemovedItem] = Field(default_factory=list)
    blocked: bool
    reason: str | None = None
