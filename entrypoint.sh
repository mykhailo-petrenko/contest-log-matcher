#!/usr/bin/env sh

PORT=${PORT:-8080}
WORKERS=${WORKERS:-2}

uvicorn api:app \
  --host 0.0.0.0 \
  --port ${PORT} \
  --workers ${WORKERS}