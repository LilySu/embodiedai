from embodied_agents.agents.runner import match_presentation_agent, run_agent, should_use_openai_agents
from embodied_agents.guardrails.output import validate_match_card_output
from embodied_agents.schemas.match import MatchPresentationInput, MatchPresentationOutput
from embodied_agents.tools.feature_diff import feature_diff
from embodied_agents.tools.pii_regex import scrub_text


async def run_match_presentation(payload: MatchPresentationInput) -> MatchPresentationOutput:
    if should_use_openai_agents():
        output = await run_agent(match_presentation_agent, payload, MatchPresentationOutput)
        return validate_match_card_output(output)

    safe_bio, _ = scrub_text(payload.candidate_bio, pre_match=True)
    excerpt = _first_sentences(safe_bio)
    features = feature_diff(payload.candidate_features, payload.shared_interests)
    card_text = f"{payload.candidate_features.activity_level.replace('_', ' ')} and {payload.candidate_features.consistency_bucket.replace('_', ' ')}. {excerpt}".strip()
    return validate_match_card_output(
        MatchPresentationOutput(card_text=card_text, displayed_features=features, excerpt=excerpt)
    )


def _first_sentences(text: str) -> str:
    if not text:
        return "Enjoys staying active and meeting for relaxed coffee conversations."
    sentences = [part.strip() for part in text.replace("!", ".").replace("?", ".").split(".") if part.strip()]
    return ". ".join(sentences[:2])[:220].strip() + "."
