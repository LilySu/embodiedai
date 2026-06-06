import type { MessageInput, MessageOutput } from "@embodied/shared-types/message";

import { appEnv } from "../platform/env";

export async function screenMessage(input: MessageInput, clerkToken: string): Promise<MessageOutput> {
  const response = await fetch(appEnv.invokeAgentUrl, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      authorization: `Bearer ${clerkToken}`
    },
    body: JSON.stringify({
      request_type: "message_relay",
      viewer_pseudo_id: input.sender_pseudo_id,
      payload: input
    })
  });

  if (!response.ok) {
    throw new Error(`agent_invoke_failed:${response.status}`);
  }

  const body = await response.json();
  return body.output as MessageOutput;
}
