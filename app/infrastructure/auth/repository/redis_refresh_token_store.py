from redis import Redis

from app.domain.auth.repository.refresh_token_store import RefreshTokenStore


class RedisRefreshTokenStore(RefreshTokenStore):
    def __init__(self, redis:Redis):
        self.redis = redis

    async def save(self, user_id:int, token:str):
        key =f"refresh_token:{user_id}"
        await self.redis.set(key, token, ex= 60*60*24*7)

    async def get(self, user_id:int) -> str | None:
        key =f"refresh_token:{user_id}"
        return await self.redis.get(key)