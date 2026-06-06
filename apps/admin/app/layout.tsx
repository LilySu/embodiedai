import type { Metadata } from "next";
import { ClerkProvider } from "@clerk/nextjs";

export const metadata: Metadata = {
  title: "Embodied Coffee Admin",
  description: "Closed-alpha support and operations dashboard"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body style={{ margin: 0, fontFamily: "Arial, sans-serif", background: "#f7f5ef", color: "#24342f" }}>
          {children}
        </body>
      </html>
    </ClerkProvider>
  );
}
