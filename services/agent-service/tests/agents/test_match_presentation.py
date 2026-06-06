import asyncio

from embodied_agents.agents.match_presentation import run_match_presentation
from embodied_agents.schemas.match import ActivityFeatureVector, MatchPresentationInput


def features() -> ActivityFeatureVector:
    return ActivityFeatureVector(
        activity_level="active",
        step_bucket="6k_10k",
        consistency_bucket="most_days",
        preferred_activity_types=["walking"],
        metro_region="San Diego",
        age_bucket="65_69",
    )


def test_match_card_uses_coarse_features() -> None:
    output = asyncio.run(run_match_presentation(
        MatchPresentationInput(
            viewer_pseudo_id="viewer_123",
            candidate_pseudo_id="candidate_123",
            candidate_features=features(),
            candidate_bio="Enjoys walks and coffee chats.",
            shared_interests=["walking"],
        )
    ))

    assert "active" in output.card_text
    assert "Distance: within your metro area" in output.displayed_features


def test_match_card_scrubs_bio_as_pre_match() -> None:
    output = asyncio.run(run_match_presentation(
        MatchPresentationInput(
            viewer_pseudo_id="viewer_123",
            candidate_pseudo_id="candidate_123",
            candidate_features=features(),
            candidate_bio="Mary enjoys walks before coffee.",
        )
    ))

    assert "Mary" not in output.card_text
    assert "[removed first_name]" in output.card_text


def test_match_card_allows_coarse_bucket_digits_if_rendered() -> None:
    output = asyncio.run(run_match_presentation(
        MatchPresentationInput(
            viewer_pseudo_id="viewer_123",
            candidate_pseudo_id="candidate_123",
            candidate_features=features(),
            candidate_bio="Enjoys the 3k_6k walking group.",
        )
    ))

    assert "3k_6k" in output.card_text
