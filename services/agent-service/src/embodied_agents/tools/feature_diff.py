from embodied_agents.schemas.match import ActivityFeatureVector


def feature_diff(candidate: ActivityFeatureVector, shared_interests: list[str]) -> list[str]:
    features = [
        f"Activity: {candidate.activity_level.replace('_', ' ')}",
        f"Routine: {candidate.consistency_bucket.replace('_', ' ')}",
        "Distance: within your metro area",
    ]
    if shared_interests:
        features.append("Shared interests: " + ", ".join(shared_interests[:3]))
    return features
