from typing import Literal

from pydantic import BaseModel, Field


class ActivityFeatureVector(BaseModel):
    activity_level: Literal["low", "moderate", "active", "very_active"]
    step_bucket: Literal["under_3k", "3k_6k", "6k_10k", "over_10k"]
    consistency_bucket: Literal["occasional", "some_days", "most_days", "daily"]
    preferred_activity_types: list[str] = Field(default_factory=list, max_length=8)
    metro_region: str = Field(min_length=2, max_length=80)
    age_bucket: Literal["60_64", "65_69", "70_74", "75_79", "80_plus"]


class MatchPresentationInput(BaseModel):
    viewer_pseudo_id: str = Field(min_length=8, max_length=128)
    candidate_pseudo_id: str = Field(min_length=8, max_length=128)
    candidate_features: ActivityFeatureVector
    candidate_bio: str = Field(default="", max_length=1200)
    shared_interests: list[str] = Field(default_factory=list, max_length=8)


class MatchPresentationOutput(BaseModel):
    card_text: str
    displayed_features: list[str] = Field(default_factory=list)
    excerpt: str
