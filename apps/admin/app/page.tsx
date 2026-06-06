import Link from "next/link";

const links = [
  { href: "/support", label: "Support triage" },
  { href: "/kyc-review", label: "KYC review" },
  { href: "/curated-matches", label: "Curated matches" }
];

export default function AdminHome() {
  return (
    <main style={{ maxWidth: 960, margin: "0 auto", padding: 32 }}>
      <h1 style={{ fontSize: 36 }}>Embodied Coffee Admin</h1>
      <nav style={{ display: "grid", gap: 12 }}>
        {links.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            style={{
              minHeight: 56,
              display: "flex",
              alignItems: "center",
              border: "2px solid #24594c",
              borderRadius: 8,
              padding: "0 18px",
              color: "#24594c",
              fontSize: 20,
              fontWeight: 700,
              textDecoration: "none",
              background: "#fff"
            }}
          >
            {link.label}
          </Link>
        ))}
      </nav>
    </main>
  );
}
