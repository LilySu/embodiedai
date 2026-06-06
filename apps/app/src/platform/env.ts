import Constants from "expo-constants";

type AppExtra = {
  clerkPublishableKey?: string;
  supabaseUrl?: string;
  supabaseAnonKey?: string;
  personaTemplateId?: string;
  vitalEnv?: string;
};

const extra = (Constants.expoConfig?.extra ?? {}) as AppExtra;
const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;
const clerkPublishableKey = process.env.EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY;

function requirePublicEnv(name: string, value: string | undefined): string {
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
}

export const appEnv = {
  clerkPublishableKey: requirePublicEnv(
    "EXPO_PUBLIC_CLERK_PUBLISHABLE_KEY",
    clerkPublishableKey ?? extra.clerkPublishableKey
  ),
  supabaseUrl: requirePublicEnv("EXPO_PUBLIC_SUPABASE_URL", supabaseUrl ?? extra.supabaseUrl),
  supabaseAnonKey: requirePublicEnv("EXPO_PUBLIC_SUPABASE_ANON_KEY", supabaseAnonKey ?? extra.supabaseAnonKey),
  invokeAgentUrl: `${requirePublicEnv("EXPO_PUBLIC_SUPABASE_URL", supabaseUrl ?? extra.supabaseUrl).replace(/\/$/, "")}/functions/v1/invoke-agent`,
  vitalEnv: process.env.EXPO_PUBLIC_VITAL_ENV ?? extra.vitalEnv ?? "sandbox",
  personaTemplateId: process.env.EXPO_PUBLIC_PERSONA_TEMPLATE_ID ?? extra.personaTemplateId
};
