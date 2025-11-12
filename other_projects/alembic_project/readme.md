

```bash

alembic revision --autogenerate -m "initial migration"
alembic upgrade head

# Rollback (Undo Last Migration)
alembic downgrade -1

```


| Command                                    | Meaning                                              | Usage                               |
| ------------------------------------------ | ---------------------------------------------------- | ----------------------------------- |
| `alembic revision -m "msg"`                | Create **empty** migration file (manual edits)       | When you want to write SQL manually |
| `alembic revision --autogenerate -m "msg"` | Create migration by **diffing models with DB**       | When models changed                 |
| `alembic upgrade head`                     | Apply **all pending migrations**                     | Deploying / local dev               |
| `alembic upgrade <revision>`               | Upgrade to a **specific migration**                  | Version control for DB              |
| `alembic downgrade -1`                     | Rollback **last migration**                          | Undo mistake                        |
| `alembic downgrade <revision>`             | Rollback to specified version                        | Reset database to stable state      |
| `alembic history`                          | Show all migrations in order                         | View list                           |
| `alembic current`                          | Shows the **current version** of DB                  | Debug                               |
| `alembic heads`                            | Show latest revision(s)                              | If multiple heads exist             |
| `alembic branches`                         | Check for **multiple migration branches**            | When conflicts occur                |
| `alembic stamp head`                       | Mark DB as up-to-date **without running migrations** | When DB existed before Alembic      |
