from app.domain.user.entity import User
from app.domain.user.repository import UserRepository
from app.domain.user.social_user import SocialUser


class CreateOrGetSocialUserUseCase:
    def __init__(self, repository:UserRepository):
        self.repository = repository

    async def execute(self, social_user: SocialUser) -> User:
        user = await self.repository.get_by_uid(social_user.uid, social_user.provider)
        if user:
            return user

        user = await self.repository.create(
            User(
                uid=social_user.uid,
                provider=social_user.provider,
                email=social_user.email,
                nickname=social_user.nickname
            )
        )
        return user

