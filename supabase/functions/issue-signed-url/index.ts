type SignedUrlRequest = {
  bucket: string;
  path: string;
  expires_in_seconds?: number;
};

const corsHeaders = {
  "access-control-allow-origin": "*",
  "access-control-allow-headers": "authorization, x-client-info, apikey, content-type",
  "access-control-allow-methods": "POST, OPTIONS"
};

Deno.serve(async (request) => {
  if (request.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  if (request.method !== "POST") {
    return json({ error: "method_not_allowed" }, 405);
  }

  const authorization = request.headers.get("authorization");
  if (!authorization?.startsWith("Bearer ")) {
    return json({ error: "missing_bearer_token" }, 401);
  }

  let body: SignedUrlRequest;
  try {
    body = await request.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  if (!isSignedUrlRequest(body)) {
    return json({ error: "invalid_signed_url_request" }, 400);
  }

  return json({ error: "storage_signing_not_configured" }, 501);
});

function isSignedUrlRequest(value: unknown): value is SignedUrlRequest {
  if (!value || typeof value !== "object") return false;
  const candidate = value as Record<string, unknown>;
  const expires = candidate.expires_in_seconds;
  return (
    typeof candidate.bucket === "string" &&
    typeof candidate.path === "string" &&
    (expires === undefined || (typeof expires === "number" && expires > 0 && expires <= 900))
  );
}

function json(body: Record<string, unknown>, status: number): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      ...corsHeaders,
      "content-type": "application/json"
    }
  });
}
