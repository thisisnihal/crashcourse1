from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import router
from db import engine, async_session
from users_service import insert_sample_users, create_users_table
from sqlalchemy import select
from models import User
from dotenv import load_dotenv

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    await create_users_table(engine)

    async with async_session() as session:
        result = await session.execute(select(User).limit(1))
        if not result.scalar_one_or_none():
            await insert_sample_users(session)
            print("Sample users inserted.")
        else:
            print("Users already exist.")

    # handover control to FastAPI runtime
    yield

    print("Application shutting down.")


app = FastAPI(title="Fast API Test", lifespan=lifespan)

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def home():
    return {"status": "ok"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
