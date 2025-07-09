from pydantic import EmailStr, BaseModel

from app.domain.user.entity import User


class LoginRequest(BaseModel):
    code: str


