# Privacy

Embodied Coffee is designed so raw biometrics and direct contact details do not need to live on our server for matching.

## What Leaves Your Device

Your app converts wearable and phone activity data into broad activity categories before sending anything to the server. The server receives coarse matching features, your metro area, an age bucket, interests, and profile text that you choose to submit.

## What Stays On Your Device

Your real name, phone number, address, and contact-exchange details are stored in an encrypted vault on your device. They are shared with another person only after mutual match acceptance.

## OpenAI Use

We use OpenAI only for two privacy-sensitive flows: screening messages before delivery and preparing privacy-safe match-card text. We do not use OpenAI to rewrite bios, explain every match, or analyze raw biometrics.

For the MVP, we use the standard OpenAI API tier, not a zero-data-retention contract. Even after our local scrubbing, agent-bound text may be retained by OpenAI for abuse monitoring according to OpenAI's standard retention terms. This is a known MVP limitation.

## Important Limitations

Embodied Coffee v1 does not include romance-scam or financial-scam detection. Do not send money, bank details, verification codes, gift cards, or sensitive documents to anyone you meet through the app. We show a safety primer during onboarding, but scam moderation is planned for a later version.

We also cannot protect against subpoenas to third-party providers, wearable vendor practices before data reaches the app, or details you voluntarily type into your public bio.
