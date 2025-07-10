from abc import ABC, abstractmethod

from app.domain.auth.entity.social_user import SocialUser


class SocialLoginStrategy(ABC):
    @abstractmethod
    async def get_user(self, code: str) -> SocialUser:
        pass