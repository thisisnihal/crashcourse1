from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData, text

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), nullable=False, unique=True),
    Column("hashed_password", String(255), nullable=False),
    Column("is_active", Boolean, nullable=False, server_default=text("TRUE")),
    Column(
        "created_at", DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    ),
    Column("role", String(50), nullable=False, server_default=text("'user'")),
)
