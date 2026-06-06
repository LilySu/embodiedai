from embodied_agents.schemas.match import MatchPresentationOutput
from embodied_agents.schemas.message import MessageOutput
from embodied_agents.tools.pii_regex import FIRST_NAME_PATTERN, pii_regex_scan


def validate_message_output(output: MessageOutput, *, pre_match: bool) -> MessageOutput:
    findings = pii_regex_scan(output.scrubbed_text, include_names=pre_match, include_time=pre_match)
    if findings:
        return MessageOutput(
            scrubbed_text="",
            removed=output.removed,
            blocked=True,
            reason="output_pii_detected",
        )
    if pre_match and FIRST_NAME_PATTERN.search(output.scrubbed_text):
        return MessageOutput(scrubbed_text="", removed=output.removed, blocked=True, reason="pre_match_name_detected")
    return output


def validate_match_card_output(output: MatchPresentationOutput) -> MatchPresentationOutput:
    text = " ".join([output.card_text, output.excerpt, " ".join(output.displayed_features)])
    if pii_regex_scan(text, include_names=False, include_time=True):
        raise ValueError("match_card_pii_detected")
    return output
