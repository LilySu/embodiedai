import type { PropsWithChildren } from "react";
import { ClerkProvider } from "@clerk/clerk-expo";

import { appEnv } from "./env";

export function AppProviders({ children }: PropsWithChildren) {
  return <ClerkProvider publishableKey={appEnv.clerkPublishableKey}>{children}</ClerkProvider>;
}
