from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = True
    role: str = "user"
    created_at: Optional[datetime] = None


class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime
    role: str

    class Config:
        orm_mode = True
