from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=False, future=True)


async def get_db_connection() -> AsyncConnection:
    async with engine.connect() as conn:
        yield conn
