import { Link } from "expo-router";
import { Text, View } from "react-native";

import { PrimaryButton } from "../../src/ui/PrimaryButton";
import { Screen } from "../../src/ui/Screen";

export default function WearablesScreen() {
  return (
    <Screen>
      <View style={{ gap: 18 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Connect activity</Text>
        <Text style={{ fontSize: 20, lineHeight: 30, color: "#2f3f39" }}>Choose how you want to share broad activity patterns.</Text>
        <PrimaryButton label="Connect wearable" />
        <PrimaryButton label="Enter manually" variant="secondary" />
        <Link href="/(onboarding)/profile" asChild>
          <PrimaryButton label="Continue" />
        </Link>
      </View>
    </Screen>
  );
}
