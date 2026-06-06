export type WearableProvider = "apple_health" | "health_connect" | "strava" | "oura" | "fitbit" | "garmin" | "whoop";

export async function connectWearable(provider: WearableProvider): Promise<void> {
  void provider;
  throw new Error("vital_native_sdk_not_configured");
}
