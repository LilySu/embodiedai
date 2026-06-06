import { Text, View } from "react-native";

import { Screen } from "../../src/ui/Screen";

export default function SettingsScreen() {
  return (
    <Screen>
      <View style={{ gap: 16 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Settings</Text>
        <Text style={{ fontSize: 20, lineHeight: 30, color: "#2f3f39" }}>Account, privacy, and support.</Text>
      </View>
    </Screen>
  );
}
