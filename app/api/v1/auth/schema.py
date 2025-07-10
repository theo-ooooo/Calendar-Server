from pydantic import BaseModel


class LoginRequest(BaseModel):
    code: str




class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str