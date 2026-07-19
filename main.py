from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.connection import Base, engine
from models import AuthToken
from routers.auth import router as auth_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"health": "ok"}
