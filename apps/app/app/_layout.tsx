import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Stack } from "expo-router";
import { useState } from "react";

import { AppProviders } from "../src/platform/AppProviders";

export default function RootLayout() {
  const [queryClient] = useState(() => new QueryClient());

  return (
    <QueryClientProvider client={queryClient}>
      <AppProviders>
        <Stack
          screenOptions={{
            headerTitleStyle: { fontSize: 22 },
            headerBackTitle: "Back",
            contentStyle: { backgroundColor: "#fbfaf7" }
          }}
        >
          <Stack.Screen name="index" options={{ title: "Embodied Coffee" }} />
          <Stack.Screen name="(auth)" options={{ headerShown: false }} />
          <Stack.Screen name="(onboarding)" options={{ title: "Onboarding" }} />
          <Stack.Screen name="(main)" options={{ headerShown: false }} />
        </Stack>
      </AppProviders>
    </QueryClientProvider>
  );
}
