def setup_weave() -> None:
    try:
        import weave

        weave.init("embodied-coffee-agent-service")
    except Exception:
        # Observability must never block privacy guardrails or request handling.
        return
