import uvicorn
from fastapi import FastAPI

from embodied_agents.api.routes import router
from embodied_agents.observability.otel_setup import setup_otel
from embodied_agents.observability.weave_setup import setup_weave

app = FastAPI(title="Embodied Coffee Agent Service", version="0.1.0")
app.include_router(router)
setup_weave()
setup_otel(app)


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


def main() -> None:
    uvicorn.run("embodied_agents.api.main:app", host="0.0.0.0", port=8080)
