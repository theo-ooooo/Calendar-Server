from app.domain.auth.repository.refresh_token_store import RefreshTokenStore
from app.domain.auth.service.token_service import TokenService


class CreateTokenPairUseCase:
    def __init__(
            self,
            token_service: TokenService,
            refresh_token_store: RefreshTokenStore
    ):
        self.token_service = token_service
        self.refresh_token_store = refresh_token_store

    async def execute(self, user_id:int) -> tuple[str, str]:
        access = self.token_service.create_access_token(user_id)
        refresh = self.token_service.refresh_access_token(user_id)
        await self.refresh_token_store.save(user_id, refresh)
        return access, refresh