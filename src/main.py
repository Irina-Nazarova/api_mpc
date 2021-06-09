import uvicorn

from fastapi import FastAPI
from core.config import settings
from db.base import databases

app = FastAPI(title="API for DB")


@app.on_event("startup")
async def startup():
    await databases.connect()


@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=settings.SERVER_PORT, host=settings.SERVER_HOST, reload=True)