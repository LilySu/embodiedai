import { z } from "zod";

import { activityFeatureVectorSchema } from "./featureVector";

export const matchPresentationInputSchema = z.object({
  viewer_pseudo_id: z.string().min(8).max(128),
  candidate_pseudo_id: z.string().min(8).max(128),
  candidate_features: activityFeatureVectorSchema,
  candidate_bio: z.string().max(1200).default(""),
  shared_interests: z.array(z.string()).max(8).default([])
});

export const matchPresentationOutputSchema = z.object({
  card_text: z.string(),
  displayed_features: z.array(z.string()).default([]),
  excerpt: z.string()
});

export type MatchPresentationInput = z.infer<typeof matchPresentationInputSchema>;
export type MatchPresentationOutput = z.infer<typeof matchPresentationOutputSchema>;
