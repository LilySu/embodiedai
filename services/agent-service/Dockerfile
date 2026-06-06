FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY services/agent-service ./services/agent-service
RUN pip install --no-cache-dir .

EXPOSE 8080
CMD ["uvicorn", "embodied_agents.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
