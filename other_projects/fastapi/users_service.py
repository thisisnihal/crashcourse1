from sqlalchemy import select
from security import hash_password
from models import User


async def create_users_table(engine):
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)


async def insert_sample_users(session):
    sample_users = [
        User(
            email="admin@example.com",
            hashed_password=hash_password("admin123"),
            role="admin",
        ),
        User(
            email="user1@example.com",
            hashed_password=hash_password("user123"),
            role="user",
        ),
        User(
            email="user2@example.com",
            hashed_password=hash_password("user456"),
            role="user",
        ),
    ]

    for user in sample_users:
        session.add(user)

    await session.commit()


async def get_all_users(session):
    result = await session.execute(
        select(User.id, User.email, User.is_active, User.created_at, User.role)
    )
    return result.mappings().all()


async def get_user_by_email(session, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def create_user(session, email: str, password: str, role: str = "user"):
    hashed_pwd = hash_password(password)
    new_user = User(email=email, hashed_password=hashed_pwd, role=role)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
