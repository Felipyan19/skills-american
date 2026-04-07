FROM python:3.11-slim

WORKDIR /app

COPY server/ ./server/
COPY catalog/ ./catalog/
COPY docs/ ./docs/

ENV PYTHONUNBUFFERED=1

EXPOSE 5050

CMD ["python", "-m", "server.http_server"]
