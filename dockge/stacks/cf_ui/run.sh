#!/usr/bin/env bash

# Run the FastAPI application with auto-reload for development
uvicorn main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --reload-dir . \
    --log-level info
