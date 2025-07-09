from datetime import timedelta, datetime

from jose import jwt

from app.domain.auth.token_service import TokenService
from app.infrastructure.config import settings


class JwtTokenService(TokenService):
    def create_access_token(self, user_id: int) -> str:
        expire:datetime = datetime.utcnow() + timedelta(minutes=60)
        payload:dict = {"sub": user_id, "exp": expire}
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

    def refresh_access_token(self, user_id: int) -> str:
        expire: datetime = datetime.utcnow() + timedelta(days=7)
        payload: dict = {"sub": user_id, "exp": expire}
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)