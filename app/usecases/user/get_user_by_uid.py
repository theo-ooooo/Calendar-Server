from app.api.v1.auth.schema import UserResponse
from app.domain.user.repository.user_repository import UserRepository

class GetUserByUIDUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, uid: str, provider: str) -> UserResponse | None:
        user = await self.repository.get_by_uid(uid, provider)

        if not user:
            return None

        return UserResponse.from_entity(user)
