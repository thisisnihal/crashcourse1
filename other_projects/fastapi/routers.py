from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db_session
from users_service import get_all_users, get_user_by_email, create_user
from user_schema import UserOut, UserCreate

router = APIRouter()


@router.get("/", response_model=list[UserOut])
async def list_users(session: AsyncSession = Depends(get_db_session)):
    users = await get_all_users(session)
    return users


@router.post("/register", response_model=UserOut)
async def register_user(
    user: UserCreate, session: AsyncSession = Depends(get_db_session)
):
    existing = await get_user_by_email(session, user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    new_user = await create_user(session, user.email, user.password, user.role)
    return new_user
