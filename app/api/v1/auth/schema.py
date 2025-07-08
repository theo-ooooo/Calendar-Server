from typing import Optional

from pydantic import EmailStr, BaseModel

from app.domain.user.entity import User


class LoginRequest(BaseModel):
    uid: str
    email: Optional[EmailStr] = None
    nickname: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    uid: str
    provider: str
    email: str | None
    nickname: str | None

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return cls(**user.__dict__)

