import { z } from "zod";

export const activityFeatureVectorSchema = z.object({
  activity_level: z.enum(["low", "moderate", "active", "very_active"]),
  step_bucket: z.enum(["under_3k", "3k_6k", "6k_10k", "over_10k"]),
  consistency_bucket: z.enum(["occasional", "some_days", "most_days", "daily"]),
  preferred_activity_types: z.array(z.string()).max(8),
  metro_region: z.string().min(2).max(80),
  age_bucket: z.enum(["60_64", "65_69", "70_74", "75_79", "80_plus"]),
});

export type ActivityFeatureVector = z.infer<typeof activityFeatureVectorSchema>;
