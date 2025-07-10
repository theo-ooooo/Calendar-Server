from abc import ABC, abstractmethod


class RefreshTokenStore(ABC):
    @abstractmethod
    async def save(self, user_id:int, refresh_token:str):
        pass

    @abstractmethod
    async def get(self, user_id:int) -> str:
        pass