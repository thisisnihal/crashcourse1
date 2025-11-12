""""""

from fastapi import FastAPI
from routers import router
from db import engine
from users_service import insert_sample_users, create_users_table
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()
app = FastAPI(title="Fast API Test")


@app.on_event("startup")
async def startup_event():
    async with engine.connect() as conn:
        await create_users_table(conn)
        result = await conn.execute(text("SELECT 1 FROM users LIMIT 1;"))
        if not result.first():
            await insert_sample_users(conn)
            print("startup done")
        await conn.commit()


app.include_router(router, prefix="/api/v1")


@app.get("/")
async def home():
    return {"status": "ok"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
