import { Text, TextInput, View } from "react-native";

import { Screen } from "../../src/ui/Screen";

export default function MessagesScreen() {
  return (
    <Screen>
      <View style={{ gap: 16 }}>
        <Text style={{ fontSize: 28, fontWeight: "700", color: "#24342f" }}>Messages</Text>
        <TextInput
          accessibilityLabel="Message text"
          placeholder="Type a message for privacy screening."
          style={{
            borderWidth: 2,
            borderColor: "#52645d",
            borderRadius: 8,
            padding: 16,
            fontSize: 20,
            backgroundColor: "#ffffff"
          }}
        />
      </View>
    </Screen>
  );
}
