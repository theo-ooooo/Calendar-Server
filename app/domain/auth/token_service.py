from abc import ABC, abstractmethod
from typing import Any, Dict


class TokenService(ABC):
    @abstractmethod
    def create_access_token(self, user_id: int) -> str:
        pass

    @abstractmethod
    def refresh_access_token(self, user_id: int) -> str:
        pass


    @abstractmethod
    def verify_token(self, token: str) -> Dict[str, Any]:
        pass