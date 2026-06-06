export type WearableProvider = "strava" | "oura" | "fitbit" | "garmin" | "whoop" | "manual";

export async function connectWearable(provider: WearableProvider): Promise<void> {
  void provider;
  throw new Error("vital_link_widget_not_configured");
}
