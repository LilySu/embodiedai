type InvokeBody = {
  request_type: "message_relay" | "match_presentation";
  viewer_pseudo_id: string;
  payload: Record<string, unknown>;
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

  let body: InvokeBody;
  try {
    body = await request.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  if (!isInvokeBody(body)) {
    return json({ error: "invalid_agent_request" }, 400);
  }

  const agentServiceUrl = Deno.env.get("AGENT_SERVICE_URL");
  if (!agentServiceUrl) {
    return json({ error: "agent_service_not_configured" }, 500);
  }

  const response = await fetch(new URL("/v1/agents/invoke", agentServiceUrl), {
    method: "POST",
    headers: {
      authorization,
      "content-type": "application/json"
    },
    body: JSON.stringify(body)
  });

  return new Response(await response.text(), {
    status: response.status,
    headers: {
      ...corsHeaders,
      "content-type": response.headers.get("content-type") ?? "application/json"
    }
  });
});

function isInvokeBody(value: unknown): value is InvokeBody {
  if (!value || typeof value !== "object") return false;
  const candidate = value as Record<string, unknown>;
  return (
    (candidate.request_type === "message_relay" || candidate.request_type === "match_presentation") &&
    typeof candidate.viewer_pseudo_id === "string" &&
    !!candidate.payload &&
    typeof candidate.payload === "object"
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
