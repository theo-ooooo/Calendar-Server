

"""
 리프레쉬 토큰으로 토큰 재발급
"""
from fastapi import HTTPException
from starlette import status

from app.domain.auth.repository.refresh_token_store import RefreshTokenStore
from app.domain.auth.service.token_service import TokenService


class ReIssueTokenUseCase:
    def __init__(self, token_service:TokenService, refresh_token_store: RefreshTokenStore):
        self.token_service = token_service
        self.refresh_token_store = refresh_token_store

    async def execute(self, refresh_token:str) -> tuple[str, str]:
        payload = self.token_service.verify_token(refresh_token)

        user_id = int(payload.get("sub"))
        print("user_id", user_id)
        stored_token = await self.refresh_token_store.get(user_id)

        print("stored_token", stored_token)

        if stored_token != refresh_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

        access = self.token_service.create_access_token(user_id)
        refresh = self.token_service.refresh_access_token(user_id)
        await self.refresh_token_store.save(user_id, refresh)
        return access, refresh

