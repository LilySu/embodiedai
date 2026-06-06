import { activityFeatureVectorSchema, type ActivityFeatureVector } from "@embodied/shared-types/featureVector";

export type RawActivitySummary = {
  averageDailySteps: number;
  activeDaysPerWeek: number;
  preferredActivityTypes: string[];
  metroRegion: string;
  age: number;
};

export function coarsenActivity(summary: RawActivitySummary): ActivityFeatureVector {
  const vector: ActivityFeatureVector = {
    activity_level: activityLevel(summary.averageDailySteps),
    step_bucket: stepBucket(summary.averageDailySteps),
    consistency_bucket: consistencyBucket(summary.activeDaysPerWeek),
    preferred_activity_types: summary.preferredActivityTypes.slice(0, 8),
    metro_region: summary.metroRegion,
    age_bucket: ageBucket(summary.age)
  };
  return activityFeatureVectorSchema.parse(vector);
}

export function assertKAnonymous(peerCount: number, k = 10): void {
  if (peerCount < k) {
    throw new Error("feature_vector_not_k_anonymous");
  }
}

function activityLevel(steps: number): ActivityFeatureVector["activity_level"] {
  if (steps < 3000) return "low";
  if (steps < 6000) return "moderate";
  if (steps < 10000) return "active";
  return "very_active";
}

function stepBucket(steps: number): ActivityFeatureVector["step_bucket"] {
  if (steps < 3000) return "under_3k";
  if (steps < 6000) return "3k_6k";
  if (steps < 10000) return "6k_10k";
  return "over_10k";
}

function consistencyBucket(days: number): ActivityFeatureVector["consistency_bucket"] {
  if (days < 2) return "occasional";
  if (days < 4) return "some_days";
  if (days < 7) return "most_days";
  return "daily";
}

function ageBucket(age: number): ActivityFeatureVector["age_bucket"] {
  if (age < 65) return "60_64";
  if (age < 70) return "65_69";
  if (age < 75) return "70_74";
  if (age < 80) return "75_79";
  return "80_plus";
}
