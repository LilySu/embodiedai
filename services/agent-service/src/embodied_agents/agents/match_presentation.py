from embodied_agents.guardrails.output import validate_match_card_output
from embodied_agents.schemas.match import MatchPresentationInput, MatchPresentationOutput
from embodied_agents.tools.feature_diff import feature_diff
from embodied_agents.tools.pii_regex import scrub_text


async def run_match_presentation(payload: MatchPresentationInput) -> MatchPresentationOutput:
    safe_bio, _ = scrub_text(payload.candidate_bio, pre_match=False)
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
