from abc import ABC, abstractmethod


class TokenService(ABC):
    @abstractmethod
    def create_access_token(self, user_id: int) -> str:
        pass

    @abstractmethod
    def refresh_access_token(self, user_id: int) -> str:
        pass
