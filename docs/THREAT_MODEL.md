# Threat Model

## Protected Assets

- Real identity and contact details in the on-device vault.
- Raw biometric streams from wearable providers.
- Pseudonymous profile and match data in Supabase.
- Message and match-card text before recipient display.

## Main Controls

- On-device coarsening before server submission.
- Pseudonymous `pseudo_id` identifiers in Supabase.
- Clerk JWT binding at the agent-service boundary.
- Deterministic PII regex scans before and after agent processing.
- Privacy redaction before Weave or OpenTelemetry export.

## Explicit MVP Gaps

- Romance and financial scam detection are deferred.
- OpenAI zero-data-retention is deferred.
- Video verification before first meet is deferred.
- Phone support and insurance are deferred.
