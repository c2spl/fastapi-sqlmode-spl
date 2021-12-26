#!/bin/sh

exec /env/bin/gunicorn \
    app.main:app \
    --bind ${HOST}:${PORT} \
    --worker-class uvicorn.workers.UvicornWorker