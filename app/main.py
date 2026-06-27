from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my little service"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"version": "1.0.0"}


@app.get("/time")
async def time():
    return {"time": datetime.now(timezone.utc).isoformat()}
