from pydantic import BaseModel


class LoginRequest(BaseModel):
    code: str




class TokenResponse(BaseModel):
    accessToken: str
    refreshToken: str