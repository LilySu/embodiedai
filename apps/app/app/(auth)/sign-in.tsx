import { Link } from "expo-router";
import { Text, TextInput, View } from "react-native";

import { PrimaryButton } from "../../src/ui/PrimaryButton";
import { Screen } from "../../src/ui/Screen";

export default function SignInScreen() {
  return (
    <Screen>
      <View style={{ gap: 16 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Sign in</Text>
        <TextInput
          accessibilityLabel="Email address"
          autoCapitalize="none"
          keyboardType="email-address"
          placeholder="Email address"
          style={{
            minHeight: 56,
            borderWidth: 2,
            borderColor: "#52645d",
            borderRadius: 8,
            paddingHorizontal: 16,
            fontSize: 20,
            backgroundColor: "#ffffff"
          }}
        />
        <Link href="/(onboarding)/age-verify" asChild>
          <PrimaryButton label="Continue" />
        </Link>
      </View>
    </Screen>
  );
}
