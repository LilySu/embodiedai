import { z } from "zod";

export const removedItemSchema = z.object({
  kind: z.string(),
  value: z.string()
});

export const messageInputSchema = z.object({
  match_id: z.string().min(8).max(128),
  sender_pseudo_id: z.string().min(8).max(128),
  recipient_pseudo_id: z.string().min(8).max(128),
  raw_text: z.string().min(1).max(2000),
  match_status: z.enum(["pre", "post"]),
  post_match_contact_consent: z.boolean().default(false)
});

export const messageOutputSchema = z.object({
  scrubbed_text: z.string().default(""),
  removed: z.array(removedItemSchema).default([]),
  blocked: z.boolean(),
  reason: z.string().nullable().default(null)
});

export type RemovedItem = z.infer<typeof removedItemSchema>;
export type MessageInput = z.infer<typeof messageInputSchema>;
export type MessageOutput = z.infer<typeof messageOutputSchema>;
