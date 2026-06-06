import { Link } from "expo-router";
import { Text, View } from "react-native";

import { PrimaryButton } from "../src/ui/PrimaryButton";
import { Screen } from "../src/ui/Screen";

export default function HomeScreen() {
  return (
    <Screen>
      <View style={{ gap: 20 }}>
        <Text style={{ fontSize: 34, fontWeight: "700", color: "#24342f" }}>
          Embodied Coffee
        </Text>
        <Text style={{ fontSize: 22, lineHeight: 32, color: "#2f3f39" }}>
          Meet nearby women for coffee through privacy-preserving activity matching.
        </Text>
        <Link href="/(auth)/sign-in" asChild>
          <PrimaryButton label="Sign in" />
        </Link>
        <Link href="/(onboarding)/age-verify" asChild>
          <PrimaryButton label="Start onboarding" variant="secondary" />
        </Link>
      </View>
    </Screen>
  );
}
