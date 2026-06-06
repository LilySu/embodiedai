from embodied_agents.guardrails.input import GuardrailError, reject_known_injection
from embodied_agents.guardrails.output import validate_message_output
from embodied_agents.schemas.message import MessageInput, MessageOutput, RemovedItem
from embodied_agents.tools.pii_regex import scrub_text


async def run_message_relay(payload: MessageInput) -> MessageOutput:
    try:
        reject_known_injection(payload.raw_text)
    except GuardrailError as exc:
        return MessageOutput(blocked=True, reason=exc.reason)

    pre_match = payload.match_status == "pre"
    scrubbed_text, findings = scrub_text(payload.raw_text, pre_match=pre_match)

    if payload.match_status == "post" and payload.post_match_contact_consent:
        # Phone and first-name sharing are allowed after mutual consent; addresses remain scrubbed.
        scrubbed_text, findings = scrub_text(payload.raw_text, pre_match=False)

    output = MessageOutput(
        scrubbed_text=scrubbed_text,
        removed=[RemovedItem(kind=finding.kind, value=finding.value) for finding in findings],
        blocked=False,
    )
    return validate_message_output(output, pre_match=pre_match)
