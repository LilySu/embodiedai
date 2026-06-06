# Embodied Coffee App

Expo universal app target for iOS, Android, and web.

Locked v1 requirements:

- Expo SDK 53+, TypeScript, Expo Router, React Native Web.
- Native auth via `@clerk/clerk-expo`; web auth via `@clerk/clerk-react`.
- Native wearables through Vital React Native SDK; web wearables through Vital Link OAuth plus manual entry.
- PII vault stays on-device.
- Only coarsened `ActivityFeatureVector` values cross the device boundary.
