import { Text, View } from "react-native";

import { Screen } from "../../src/ui/Screen";

export default function MatchesScreen() {
  return (
    <Screen>
      <View style={{ gap: 16 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Matches</Text>
        <Text style={{ fontSize: 20, lineHeight: 30, color: "#2f3f39" }}>No matches yet.</Text>
      </View>
    </Screen>
  );
}
