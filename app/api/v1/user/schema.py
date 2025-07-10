from pydantic import BaseModel

from app.domain.user.entity.user import User


class UserResponse(BaseModel):
    id: int
    uid: str
    provider: str
    email: str | None
    nickname: str | None

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return cls(**user.__dict__)