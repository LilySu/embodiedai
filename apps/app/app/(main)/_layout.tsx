import { Tabs } from "expo-router";

export default function MainLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarLabelStyle: { fontSize: 16 },
        tabBarStyle: { minHeight: 72, paddingBottom: 10, paddingTop: 8 },
        headerTitleStyle: { fontSize: 22 }
      }}
    >
      <Tabs.Screen name="matches" options={{ title: "Matches" }} />
      <Tabs.Screen name="messages" options={{ title: "Messages" }} />
      <Tabs.Screen name="settings" options={{ title: "Settings" }} />
    </Tabs>
  );
}
