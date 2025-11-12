from db import SessionLocal
from sqlalchemy import text

db = SessionLocal()


names = [
    {"name": "Nihal K"},
    {"name": "Jessica"},
    {"name": "Robert"},
    {"name": "Henry"},
]

# before adding email column
# db_response = db.execute(text("INSERT INTO users (name) VALUES (:name)"), names)


# after adding email column
names_with_emails = [
    {"name": "Kevin", "email": "kevin11@mail.com"},
    {"name": "Jhon Die", "email": "jhon@outlook.com"},
]

# db_response = db.execute(
#     text("DELETE FROM users WHERE name = (:name)"), names_with_emails
# )


db_response = db.execute(
    text("INSERT INTO users (name, email) VALUES (:name, :email)"),
    names_with_emails,
)


db.commit()
db.close()


print(f"db response: {db_response.rowcount}")
