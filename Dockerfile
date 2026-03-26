FROM python:3.11-slim

WORKDIR /app

COPY api/ ./api/

ENV PYTHONUNBUFFERED=1

EXPOSE 5050

CMD ["python", "-m", "api.http_server"]
