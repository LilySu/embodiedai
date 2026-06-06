import type { ComponentProps } from "react";
import { Pressable, Text } from "react-native";

type Props = ComponentProps<typeof Pressable> & {
  label: string;
  variant?: "primary" | "secondary";
};

export function PrimaryButton({ label, variant = "primary", style, ...props }: Props) {
  const isPrimary = variant === "primary";
  return (
    <Pressable
      accessibilityRole="button"
      style={[
        {
          minHeight: 56,
          borderRadius: 8,
          alignItems: "center",
          justifyContent: "center",
          paddingHorizontal: 20,
          backgroundColor: isPrimary ? "#24594c" : "#ffffff",
          borderWidth: 2,
          borderColor: "#24594c"
        },
        typeof style === "function" ? undefined : style
      ]}
      {...props}
    >
      <Text style={{ color: isPrimary ? "#ffffff" : "#24594c", fontSize: 20, fontWeight: "700" }}>
        {label}
      </Text>
    </Pressable>
  );
}
