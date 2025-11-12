from fastapi import APIRouter, Depends, HTTPException, status
from db import get_db_connection
from users_service import get_all_users, get_user_by_email, create_user
from user_schema import UserOut, UserCreate

router = APIRouter()


@router.get("/", response_model=list[UserOut])
async def list_users(conn=Depends(get_db_connection)):
    result = await get_all_users(conn)
    return result


@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate, conn=Depends(get_db_connection)):
    existing = await get_user_by_email(conn, user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    new_user = await create_user(conn, user.email, user.password, user.role)
    return new_user
