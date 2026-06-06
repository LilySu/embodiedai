import { Link } from "expo-router";
import { Text, View } from "react-native";

import { PrimaryButton } from "../../src/ui/PrimaryButton";
import { Screen } from "../../src/ui/Screen";

export default function AgeVerifyScreen() {
  return (
    <Screen>
      <View style={{ gap: 18 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Age verification</Text>
        <Text style={{ fontSize: 20, lineHeight: 30, color: "#2f3f39" }}>Confirm that you are 60 or older to continue.</Text>
        <Link href="/(onboarding)/wearables" asChild>
          <PrimaryButton label="Continue" />
        </Link>
      </View>
    </Screen>
  );
}
