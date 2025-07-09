from abc import ABC, abstractmethod

from app.api.v1.auth.schema import LoginRequest
from app.domain.user.social_user import SocialUser


class SocialLoginStrategy(ABC):
    @abstractmethod
    async def get_user(self, code: str) -> SocialUser:
        pass