from abc import ABC, abstractmethod


class RefreshTokenStore(ABC):
    @abstractmethod
    async def save(self, user_id:int, refresh_token:str): ...