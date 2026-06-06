import { Link } from "expo-router";
import { Text, TextInput, View } from "react-native";

import { PrimaryButton } from "../../src/ui/PrimaryButton";
import { Screen } from "../../src/ui/Screen";

export default function ProfileScreen() {
  return (
    <Screen>
      <View style={{ gap: 18 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Profile</Text>
        <TextInput
          multiline
          accessibilityLabel="Short profile bio"
          placeholder="Write a short bio without names, phone numbers, or addresses."
          style={{
            minHeight: 160,
            borderWidth: 2,
            borderColor: "#52645d",
            borderRadius: 8,
            padding: 16,
            fontSize: 20,
            lineHeight: 30,
            backgroundColor: "#ffffff"
          }}
        />
        <Link href="/(main)/matches" asChild>
          <PrimaryButton label="View matches" />
        </Link>
      </View>
    </Screen>
  );
}
