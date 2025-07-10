from app.api.v1.auth.schema import UserResponse
from app.domain.user.entity.user import User
from app.domain.user.repository.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, uid:str, provider: str, email: str | None = None) -> User:
       user = User(uid=uid, provider=provider, email=email)
       return await self.repository.create(user)


