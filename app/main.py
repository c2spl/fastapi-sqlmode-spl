from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from . import database as db
from .api.v1.route import app as router


app = FastAPI()
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()


@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"
