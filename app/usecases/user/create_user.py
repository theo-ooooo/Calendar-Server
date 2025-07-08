from app.api.v1.auth.schema import UserResponse
from app.domain.user.entity import User
from app.infrastructure.db.models import User as UserModel
from app.domain.user.repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, uid:str, provider: str, email: str | None = None) -> User:
       user = User(uid=uid, provider=provider, email=email)
       return await self.repository.create(user)


