""""""

from security import hash_password
from sqlalchemy import text
from models import users


async def create_users_table(conn):
    await conn.run_sync(users.metadata.create_all)


async def insert_sample_users(conn):
    sample_users = [
        ("admin@example.com", hash_password("admin123"), "admin"),
        ("user1@example.com", hash_password("user123"), "user"),
        ("user2@example.com", hash_password("user456"), "user"),
    ]
    for email, hashed, role in sample_users:
        await conn.execute(
            text(
                """
                INSERT INTO users (email, hashed_password, role)
                VALUES (:email, :hashed_password, :role)
                ON CONFLICT (email) DO NOTHING;
            """
            ),
            {"email": email, "hashed_password": hashed, "role": role},
        )
    await conn.commit()


async def get_all_users(conn):
    result = await conn.execute(
        text("SELECT id, email, is_active, created_at, role FROM users;")
    )
    return result.mappings().all()


async def get_user_by_email(conn, email: str):
    result = await conn.execute(
        text(
            """
            SELECT id, email, hashed_password, is_active, created_at, role
            FROM users WHERE email=:email;
        """
        ),
        {"email": email},
    )
    return result.mappings().first()


async def create_user(conn, email: str, password: str, role: str = "user"):
    hashed_pwd = hash_password(password)
    result = await conn.execute(
        text(
            """
            INSERT INTO users (email, hashed_password, role)
            VALUES (:email, :hashed_password, :role)
            RETURNING id, email, is_active, created_at, role;
        """
        ),
        {"email": email, "hashed_password": hashed_pwd, "role": role},
    )
    await conn.commit()  # important else it will rollback the transaction
    return result.mappings().first()
