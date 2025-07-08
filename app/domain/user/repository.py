from abc import abstractmethod, ABC
from typing import Optional

from .entity import User


class UserRepository(ABC):
    """소셜 로그인 기반 사용자 저장소 인터페이스"""

    @abstractmethod
    async def get_by_uid(self, uid: str, provider: str) -> Optional[User]:
        """이메일 + 소셜 제공자(provider) 기준으로 사용자 조회"""
        pass

    @abstractmethod
    async def create(self, user: User) -> User:
        """사용자 생성 (소셜 로그인 기준)"""
        pass