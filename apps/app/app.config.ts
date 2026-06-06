import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import type { ExpoConfig } from "expo/config";

loadWorkspaceEnv();

const config: ExpoConfig = {
  name: "Embodied Coffee",
  slug: "embodied-coffee",
  scheme: "embodiedcoffee",
  version: "0.1.0",
  orientation: "portrait",
  userInterfaceStyle: "light",
  platforms: ["ios", "android", "web"],
  ios: {
    bundleIdentifier: "app.embodiedcoffee.mobile",
    supportsTablet: true
  },
  android: {
    package: "app.embodiedcoffee.mobile"
  },
  web: {
    bundler: "metro",
    output: "static"
  },
  plugins: ["expo-router", "expo-secure-store", "expo-notifications"],
  experiments: {
    typedRoutes: true
  },
  extra: {
    clerkPublishableKey: process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY,
    supabaseUrl: process.env.EXPO_PUBLIC_SUPABASE_URL,
    supabaseAnonKey: process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY,
    personaTemplateId: process.env.EXPO_PUBLIC_PERSONA_TEMPLATE_ID,
    vitalEnv: process.env.EXPO_PUBLIC_VITAL_ENV ?? "sandbox"
  }
};

export default config;

function loadWorkspaceEnv() {
  const envPath = resolve(__dirname, "../../.env");
  if (!existsSync(envPath)) return;

  for (const line of readFileSync(envPath, "utf8").split(/\r?\n/)) {
    const match = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)=(.*)\s*$/);
    if (!match) continue;

    const key = match[1];
    const rawValue = match[2];
    if (!key || rawValue === undefined) continue;
    if (!key.startsWith("EXPO_PUBLIC_") || process.env[key] !== undefined) continue;

    process.env[key] = rawValue.replace(/^(['"])(.*)\1$/, "$2");
  }
}
