from pydantic import EmailStr, BaseModel

from app.domain.user.entity import User


class LoginRequest(BaseModel):
    code: str


class UserResponse(BaseModel):
    id: int
    uid: str
    provider: str
    email: str | None
    nickname: str | None

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return cls(**user.__dict__)

