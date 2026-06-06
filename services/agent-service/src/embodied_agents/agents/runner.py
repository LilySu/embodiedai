"""OpenAI Agents SDK integration point.

The deterministic implementation is used in tests and local development so the
privacy contract is enforceable without network credentials. Production can wire
the SDK Runner here while keeping the same schemas and guardrail calls.
"""

from embodied_agents.agents.triage import triage

__all__ = ["triage"]
