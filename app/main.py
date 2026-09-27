from fastapi import FastAPI
from .api import router
from .db import create_db_and_tables

app = FastAPI(title="Insurance Claim Triage Agent")
app.include_router(router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/health")
def health():
    return {"status": "ok"}
