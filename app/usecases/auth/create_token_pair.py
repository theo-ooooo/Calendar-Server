from app.domain.auth.token_service import TokenService


class CreateTokenPairUseCase:
    def __init__(self, token_service:TokenService):
        self.token_service = token_service

    def execute(self, user_id:int) -> tuple[str, str]:
        access = self.token_service.create_access_token(user_id)
        refresh = self.token_service.refresh_access_token(user_id)
        return access, refresh