import uvicorn
from fastapi import FastAPI

from core.config import settings
from endpoins import devices, users, auth
from db.base import databases

app = FastAPI(title="API for DB")
app.include_router(devices.router, prefix="/api/v1/devices", tags=["devices"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])


@app.on_event("startup")
async def startup():
    await databases.connect()


@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=settings.SERVER_PORT, host=settings.SERVER_HOST, reload=True)